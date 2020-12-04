#include <iostream>

#include <lib1/s1.h>

static const int arr[] = {
    #include <prog2/data.h>
};

int main() {
    std::cout << f1() + arr[0] << std::endl;
}
