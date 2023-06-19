#include "animal.h"

class Cat : public Animal {
  Cat(char *const name);
  void make_sound();
  void purr();
};
