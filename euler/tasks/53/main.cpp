#include <euler/lib/bigint.h>
#include <euler/lib/comb.h>

#include <iostream>

int main() {
    auto cnk = cnk_t<bigint_t>();

    int s = 0;

    for (int n = 1; n <= 100; ++n) {
        for (int k = 1; k <= n; ++k) {
            if (cnk(n, k) >= 1000000) {
                s += 1;
            }
        }
    }

    std::cout << s << std::endl;
}
