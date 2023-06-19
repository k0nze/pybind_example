#ifndef CAT_H
#define CAT_H

#include "animal.h"

class Cat : public Animal {
public:
    Cat(const std::string& name);
    void make_sound();
    void purr();
};

#endif
