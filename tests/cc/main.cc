#include <cassert>
#include <iostream>
#include <string>

#include "../../src/backend/animal.h"
#include "../../src/backend/cat.h"
#include "../../src/backend/dog.h"

int main(int argc, char* argv[]) {
    std::string animal_name = "Kahooz";
    auto animal = Animal(animal_name);
    animal.make_sound();
    assert(animal_name.compare(animal.get_name()) == 0);

    std::string dog_name = "Bello";
    auto dog = Dog(dog_name);
    dog.wag_tail();
    dog.make_sound();
    assert(dog_name.compare(dog.get_name()) == 0);

    std::string cat_name = "Simba";
    auto cat = Cat(cat_name);
    cat.purr();
    cat.make_sound();
    assert(cat_name.compare(cat.get_name()) == 0);

    return 0;
}
