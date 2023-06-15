cmake_minimum_required(VERSION 3.16)
project(test_cc CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(BACKEND_SRC_PATH "../../pybind_example/backend")

add_executable(main main.cc "${BACKEND_SRC_PATH}/test_class.cc")
