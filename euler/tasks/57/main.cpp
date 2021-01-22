#include <euler/lib/bigint.h>

#include <iostream>

int main() {
    bigint_t n = 3;
    bigint_t m = 2;

    size_t s = 0;

    for (uint i = 2; i < 1000; ++i) {
        auto m1 = n + m;
        auto n1 = m1 + m;

        if (n1.digit_count() > m1.digit_count()) {
            ++s;
        }

        n = n1;
        m = m1;
    }

    std::cout << s << std::endl;
}
