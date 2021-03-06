#include <euler/lib/euler.h>

int main() {
    size_t maxs = 0;

    for (uint a = 1; a < 100; ++a) {
        for (uint b = 1; b < 100; ++b) {
            auto sum = pow_int(bigint_t(a), b).digit_sum();

            if (sum > maxs) {
                maxs = sum;

                std::cout << maxs << std::endl;
            }
        }
    }
}
