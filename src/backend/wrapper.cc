#include <pybind11/pybind11.h>

#include <string>

#include "animal.h"
#include "cat.h"
#include "dog.h"

namespace py = pybind11;

PYBIND11_MODULE(pybind_example, m) {
    py::class_<Animal>(m, "Animal")
        .def(py::init<const std::string&>(), py::arg("name"))
        .def("get_name", &Animal::get_name)
        .def("make_sound", &Animal::make_sound);

    py::class_<Dog>(m, "Dog")
        .def(py::init<const std::string&>(), py::arg("name"))
        .def("wag_tail", &Dog::wag_tail)
        .def("make_sound", &Dog::make_sound);

    py::class_<Cat>(m, "Cat")
        .def(py::init<const std::string&>(), py::arg("name"))
        .def("purr", &Cat::purr)
        .def("make_sound", &Cat::make_sound);
}
