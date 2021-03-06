#include <euler/lib/euler.h>

int main() {
    auto calc = cnk<bigint_t>();

    uint s = 0;

    for (uint n = 1; n <= 100; ++n) {
        for (uint k = 1; k <= n; ++k) {
            if (calc(n, k) >= 1000000) {
                s += 1;
            }
        }
    }

    std::cout << s << std::endl;
}
