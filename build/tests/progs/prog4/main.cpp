#include <iostream>
#include <cstdlib>

int main() {
    free(malloc(10));

    std::cout << "main()" << std::endl;

    return 0;
}
