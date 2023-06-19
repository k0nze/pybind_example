#include "animal.h"

#include <iostream>

Animal::Animal(const std::string& name) : name_(name) {}

void Animal::make_sound() { std::cout << "nope" << std::endl; }

std::string Animal::get_name() { return this->name_; }
