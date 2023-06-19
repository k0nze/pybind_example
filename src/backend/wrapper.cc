#include <pybind11/pybind11.h>

#include "animal.h"

namespace py = pybind11;

PYBIND11_MODULE(pybind_example, m) {
  py::class_<Animal>(m, "Animal")
      .def(py::init<char *const>(), py::arg("name"))
      .def("get_name", &Animal::get_name);
}
