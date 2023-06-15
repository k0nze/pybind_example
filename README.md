# Example Project showing how to Create a Python Package with a pybind11 backend

This example project uses pybind11 as a submodule add to `external/pybind11`.

## Prerequisits

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

## Install Locally

```
git clone https://github.com/k0nze/pybind_example ${PYBIND_EXAMPLE_PATH}
cd ${INSTALL_DIR_PATH}
python -m venv .venv
source .venv/bin/activate
python -m pip install [-e] ${PYBIND_EXAMPLE_PATH}
```

## Install from github

```
cd ${INSTALL_DIR_PATH}
python -m venv .venv
source .venv/bin/activate
python -m pip install git+https://github.com/k0nze/pybind_example.git
```
