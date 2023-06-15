from .backend.pybind_example import TestClass


def run():
    tc = TestClass(42)
    return tc.get_num()


if __name__ == "__main__":
    print(run())
