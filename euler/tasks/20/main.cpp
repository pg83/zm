#include <euler/lib/bigint.h>

#include <iostream>

int main() {
    bigint_t res = 1;

    for (size_t i = 2; i < 100; ++i) {
        res *= i;
    }

    std::cout << res.dig_sum() << std::endl;
}
