#include <euler/lib/euler.h>

int main() {
    bigint_t res = 1;

    for (size_t i = 2; i < 100; ++i) {
        res *= i;
    }

    std::cout << res.digit_sum() << std::endl;
}
