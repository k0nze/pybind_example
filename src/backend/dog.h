#include "animal.h"

class Dog : public Animal {
public:
  Dog(char *const name);
  void make_sound();
  void wag_tail();
};
