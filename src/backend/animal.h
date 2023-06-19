#include <string>

class Animal {
public:
  Animal(char *const name);
  void make_sound();
  std::string get_name();

protected:
  std::string name_;
};
