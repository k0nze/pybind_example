# Example Project showing how to Create a Python Package with a pybind11 backend

This example project uses pybind11 as a submodule added to `external/pybind11`.

## Project Structure

* `src`: contains the project's Python and C++ code
* `src/backend`: contains the project's C++ code and is target for the `cpython.so` which is created during the build process
* `external`: contains the project's submodules such as `pybind11`. Submodules can be downloaded using `git submodule update --init --recursive`
* `test`: contains the project's tests
* `test/py`: contains the Python unit tests
* `test/cc`: contains the C++ tests to test the C++ code without the Python interface
* `CMakeLists.txt`: contains all build instructions for the C++ code and the `pybind11` wrapper
* `setup.py`: contains the instructions on how to put everything into a Python package including C++ compiliation

## Install

### Prerequisits

Python version `>=3.10` (lower is possible if you avoid the `match` operator)

Ubuntu:
```
sudo apt install build-essential cmake ninja-build
```

macOS:
```
xcode-select --install
brew install cmake ninja-build
```

### Install Locally

```
git clone https://github.com/k0nze/pybind_example ${PYBIND_EXAMPLE_PATH}
cd ${INSTALL_DIR_PATH}
python -m venv .venv
source .venv/bin/activate
python -m pip install [-e] ${PYBIND_EXAMPLE_PATH}
```

### Install from github

```
cd ${INSTALL_DIR_PATH}
python -m venv .venv
source .venv/bin/activate
python -m pip install git+https://github.com/k0nze/pybind_example.git
```
