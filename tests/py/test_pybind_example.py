import unittest
import pybind_example


class TestPybindExample(unittest.TestCase):
    def test_test_class(self) -> None:
        self.assertEqual(pybind_example.run(), 42)
