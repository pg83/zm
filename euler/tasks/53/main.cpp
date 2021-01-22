#include <euler/lib/bigint.h>
#include <euler/lib/cache.h>

#include <iostream>

int main() {
    auto cnk = cacher2_t<int, int, bigint_t>([](int n, int k, auto& cnk) -> bigint_t {
        if (k == 0) {
            return 1;
        }

        if (n == k) {
            return 1;
        }

        return cnk(n - 1, k - 1) + cnk(n - 1, k);
    });

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
