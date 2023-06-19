#include "cat.h"

#include <iostream>

Cat::Cat(const std::string& name) : Animal(name) {}

void Cat::make_sound() { std::cout << "meow" << std::endl; }

void Cat::purr() { std::cout << this->name_ << " purrs" << std::endl; }
