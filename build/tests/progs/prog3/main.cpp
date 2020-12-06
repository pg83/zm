#include <build/tests/libs/lib1/s1.h>
#include <build/tests/libs/lib2/s2.h>
#include <build/tests/libs/lib3/s3.h>

int main() {
    throw f1() + f2() + f3();
}
