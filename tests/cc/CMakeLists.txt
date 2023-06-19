cmake_minimum_required(VERSION 3.16)
project(test_cc CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(BACKEND_SRC_PATH ../../src/backend)

add_executable(
    test_pybind_example main.cc ${BACKEND_SRC_PATH}/animal.cc
                        ${BACKEND_SRC_PATH}/dog.cc ${BACKEND_SRC_PATH}/cat.cc)
