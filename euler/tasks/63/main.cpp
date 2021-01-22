#include <euler/lib/euler.h>

int main() {
    size_t res = 0;

    for (bigint_t a = 1; a < 30; ++a) {
        for (uint b = 1; b < 30; ++b) {
            if (pow_int(a, b).digit_count() == b) {
                ++res;
            }
        }
    }

    std::cout << res << std::endl;
}
