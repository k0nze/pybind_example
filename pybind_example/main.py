from .backend.pybind_example import TestClass

if __name__ == "__main__":
    tc = TestClass(42)
    print(f"{tc.get_num()}")
