#include <iostream>

#include <build/tests/libs/lib1/s1.h>
#include <build/tests/libs/lib2/s2.h>

int main() {
    std::cout << f1() + f2() << std::endl;
}
