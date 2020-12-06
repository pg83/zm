#include <iostream>

static struct A {
    A() {
        std::cout << "A()" << std::endl;
    }
} a;
