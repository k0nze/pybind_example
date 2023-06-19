#include <pybind11/pybind11.h>

#include "animal.h"
#include "cat.h"
#include "dog.h"

namespace py = pybind11;

PYBIND11_MODULE(pybind_example, m) {
    py::class_<Animal>(m, "Animal")
        .def(py::init<char* const>(), py::arg("name"))
        .def("get_name", &Animal::get_name);

    py::class_<Dog>(m, "Dog")
        .def(py::init<char* const>(), py::arg("name"))
        .def("get_name", &Dog::get_name)
        .def("wag_tail", &Dog::wag_tail);

    py::class_<Cat>(m, "Cat")
        .def(py::init<char* const>(), py::arg("name"))
        .def("get_name", &Cat::get_name)
        .def("purr", &Cat::purr);
}
