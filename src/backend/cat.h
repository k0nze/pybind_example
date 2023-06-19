#ifndef CAT_H
#define CAT_H

#include "animal.h"

class Cat : public Animal {
public:
    Cat(char* const name);
    void make_sound();
    void purr();
};

#endif
