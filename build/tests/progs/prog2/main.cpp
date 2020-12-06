#include <build/tests/libs/lib1/s1.h>

static const int arr[] = {
    #include <build/tests/progs/prog2/data.h>
};

int main() {
    throw f1() + arr[0];
}
