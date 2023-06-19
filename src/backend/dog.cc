#include "dog.h"

#include <iostream>

Dog::Dog(char* const name) : Animal(name) {}

void Dog::make_sound() { std::cout << "ruff" << std::endl; }

void Dog::wag_tail() { std::cout << this->name_ << " wags tail" << std::endl; }
