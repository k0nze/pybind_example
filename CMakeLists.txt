cmake_minimum_required(VERSION 3.16)
project(pybind_example CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(Git)

# download submodules if they aren't present
if(GIT_FOUND AND EXISTS "${PROJECT_SOURCE_DIR}/.git")
  # update submodules
  option(GIT_SUBMODULE "Check submodules during build" ON)
  if(GIT_SUBMODULE)
    message(STATUS "Submodule update")
    execute_process(
      COMMAND ${GIT_EXECUTABLE} submodule update --init --recursive
      WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
      RESULT_VARIABLE GIT_SUBMOD_RESULT)
    if(NOT GIT_SUBMOD_RESULT EQUAL "0")
      message(
        FATAL_ERROR
          "git submodule update --init --recursive failed with $GIT_SUBMOD_RESULT}, please check git log"
      )
    endif()
  endif()
endif()

# globally enable -fPIC
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

set(MOVE_CPYTHON_SO
    "OFF"
    CACHE STRING "cpython.so is moved into src/backend")

# tell CMake where pybind11 is
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/external/pybind11)

set(BACKEND_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src/backend)

pybind11_add_module(
  pybind_example ${BACKEND_SOURCE_DIR}/wrapper.cc
  ${BACKEND_SOURCE_DIR}/animal.cc ${BACKEND_SOURCE_DIR}/dog.cc
  ${BACKEND_SOURCE_DIR}/cat.cc)

if(MOVE_CPYTHON_SO)
  # move cpython.so into backend directory
  set_target_properties(pybind_example PROPERTIES LIBRARY_OUTPUT_DIRECTORY
                                                  ${BACKEND_SOURCE_DIR})
endif()
