from .backend.pybind_example import Animal as backend_Animal
from .backend.pybind_example import Dog as backend_Dog
from .backend.pybind_example import Cat as backend_Cat


class Animal(backend_Animal):
    def __init__(self, name) -> None:
        super().__init__(name)


class Dog(Animal, backend_Dog):
    def __init__(self, name) -> None:
        Animal.__init__(self, name)
        backend_Dog.__init__(self, name)


class Cat(Animal, backend_Cat):
    def __init__(self, name) -> None:
        Animal.__init__(self, name)
        backend_Cat.__init__(self, name)
