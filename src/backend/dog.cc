#include "dog.h"

#include <iostream>

Dog::Dog(const std::string& name) : Animal(name) {}

void Dog::make_sound() { std::cout << "ruff" << std::endl; }

void Dog::wag_tail() { std::cout << this->name_ << " wags tail" << std::endl; }
