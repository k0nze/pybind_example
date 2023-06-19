import unittest
from pybind_example import Animal, Dog, Cat


class TestPybindExample(unittest.TestCase):
    def test_animal(self) -> None:
        animal_name = "Kahooz"
        animal = Animal(animal_name)
        animal.make_sound()
        self.assertEqual(animal_name, animal.get_name())

        dog_name = "Bello"
        dog = Dog(dog_name)
        dog.wag_tail()
        dog.make_sound()
        self.assertEqual(dog_name, dog.get_name())

        cat_name = "Simba"
        cat = Cat(cat_name)
        cat.purr()
        cat.make_sound()
        self.assertEqual(cat_name, cat.get_name())

        print(isinstance(cat, Animal))
