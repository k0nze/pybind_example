#include "test_class.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(pybind_example, m) {
  py::class_<TestClass>(m, "TestClass")
      .def(py::init<int>(), py::arg("num"))
      .def("get_num", &TestClass::get_num);
}
