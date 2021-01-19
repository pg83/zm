#include <euler/lib/bigint.h>

#include <iostream>

int main() {
    bigint_t res = 1;

    for (size_t i = 2; i < 100; ++i) {
        res *= i;
    }

    size_t sum = 0;

    for (auto ch : res.to_string()) {
        sum += ch - '0';
    }

    std::cout << sum << std::endl;
}
