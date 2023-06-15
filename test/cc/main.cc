#include "../../pybind_example/backend/test_class.h"

#include <iostream>

int main(int argc, char *argv[]) {
  auto tc = TestClass(42);

  std::cout << tc.get_num() << std::endl;

  return 0;
}
