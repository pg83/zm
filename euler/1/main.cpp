#include <iostream>
#include <cstdint>

int main() {
    unsigned int res = 0;

    for (unsigned int i = 1; i < 1000; ++i) {
        if (i % 3 == 0) {
            res += i;
        } else if (i % 5 == 0) {
            res += i;
        }
    }

    std::cout << res << std::endl;
}
