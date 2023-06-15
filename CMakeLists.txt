cmake_minimum_required(VERSION 3.16)
project(pybind_example CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# globally enable -fPIC
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# tell CMake where pybind11 is
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/external/pybind11)

set(BACKEND_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/pybind_example/backend)

pybind11_add_module(pybind_example ${BACKEND_SOURCE_DIR}/wrapper.cc
                    ${BACKEND_SOURCE_DIR}/test_class.cc)

# move cpython.so into backend directory
set_target_properties(pybind_example PROPERTIES LIBRARY_OUTPUT_DIRECTORY
                                                ${BACKEND_SOURCE_DIR})
