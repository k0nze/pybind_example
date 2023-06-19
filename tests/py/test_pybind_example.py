import unittest
import pybind_example


class TestPybindExample(unittest.TestCase):
    def test_animal(self) -> None:
        name = "Kahooz"
        animal = pybind_example.Animal(name)
        self.assertEqual(name, animal.get_name())
