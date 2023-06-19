import os
import sys
import subprocess
from pathlib import Path

import distutils

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

from setuptools.command.develop import develop as develop_orig
from setuptools.command.install import install as install_orig

from shutil import which


class develop(develop_orig):
    def run(self):
        print("editable install (entry point)")
        global editable_install
        editable_install = True
        super().run()


class install(install_orig):
    def run(self):
        print("non-editable install (entry point)")
        super().run()


class CMakeExtension(Extension):
    def __init__(self, name):
        Extension.__init__(self, name, sources=[])


class CMakeBuild(build_ext):
    def run(self):
        # check if CMake is installed
        if which("cmake") is None:
            raise RuntimeError(
                "CMake must be installed to build the following extensions: "
                + ", ".join(e.name for e in self.extensions)
            )

        # get path to directory which will contain the build artifacts
        build_dir_path = os.path.abspath(self.build_temp)

        # set the CMake arguments for compiling the C++ code and pybind11 wrapper
        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={build_dir_path}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DPYBIND11_PYTHON_VERSION={sys.version_info.major}.{sys.version_info.minor}",
        ]

        # check if installation is editable
        if "editable_wheel" in sys.argv:
            global editable_install
            editable_install = True

        # get path to directory where the cpython.so will be after build
        if "editable_install" in globals():
            print("editable install")
            # get path to install directory
            self.pybind_example_backend_install_dir_path = Path(
                self.get_ext_fullpath("src")
            ).resolve()
            self.pybind_example_backend_install_dir_path = Path(
                str(self.pybind_example_backend_install_dir_path.parents[0])
                + "/src/backend/"
            )
            # in an editable install the created lib and cpython.so have to be moved into the src/backend directory
            cmake_args.append("-DMOVE_CPYTHON_SO=ON")
            cmake_args.append("-DMOVE_LIB=ON")

        else:
            print("non-editable install")
            # get path to install directory
            self.pybind_example_backend_install_dir_path = Path(
                distutils.sysconfig.get_python_lib() + "/pybind_example/backend/"
            )

        print(
            f"Install path to pybind_example/backend: {self.pybind_example_backend_install_dir_path}"
        )

        # check if installation is in debug or release mode
        if self.debug:
            build_config = "Debug"
        else:
            build_config = "Release"

        # append build config to cmake arguments
        build_args = ["--config", build_config]
        cmake_args.append(f"-DCMAKE_BUILD_TYPE={build_config}")

        # check if ninja is installed
        if which("ninja") is not None:
            cmake_args.append("-GNinja")
        else:
            # use make instead
            build_args.append("--")
            build_args.append("-j2")

        # update CXXFLAGS environment variable with operation system information
        env = os.environ.copy()
        env["CXXFLAGS"] = '{} -DVERSION_INFO=\\"{}\\"'.format(
            env.get("CXXFLAGS", ""), self.distribution.get_version()
        )

        if not os.path.exists(build_dir_path):
            os.makedirs(build_dir_path)

        # get path to CMakeLists.txt which is in the same directory as this setup.py file
        cmake_list_dir = os.path.abspath(os.path.dirname(__file__))

        # run cmake command
        print("-" * 10, "Running CMake prepare", "-" * 10)
        subprocess.check_call(
            ["cmake", cmake_list_dir] + cmake_args, cwd=build_dir_path, env=env
        )

        # emit CMake command for debugging purposes
        print(f"CMake command: cmake {cmake_list_dir} {' '.join(cmake_args)}")

        # build
        print("-" * 10, "Building extensions", "-" * 10)
        cmake_cmd = ["cmake", "--build", "."] + build_args
        subprocess.check_call(cmake_cmd, cwd=build_dir_path)

        # move cpython.so from build temp to final position
        if "editable_install" not in globals():
            for ext in self.extensions:
                self.move_output(ext)

    def move_output(self, ext):
        # move cpython.so to pybind_example/backend dir
        build_dir_path = Path(self.build_temp).resolve()

        source_path = build_dir_path / self.get_ext_filename(ext.name)

        dest_path = Path(self.get_ext_fullpath(ext.name)).resolve()
        dest_path = Path(
            str(self.pybind_example_backend_install_dir_path) + "/" + dest_path.name
        )
        dest_directory = dest_path.parents[0]
        dest_directory.mkdir(parents=True, exist_ok=True)
        self.copy_file(source_path, dest_path)


ext_modules = [
    CMakeExtension("pybind_example"),
]

setup(
    name="pybind_example",
    version="0.1.0",
    packages=["pybind_example", "pybind_example.backend"],
    package_dir={
        "pybind_example": "src",
        "pybind_example.backend": "src/backend",
    },
    ext_modules=ext_modules,
    cmdclass={"develop": develop, "install": install, "build_ext": CMakeBuild},
    zip_safe=False,
)
