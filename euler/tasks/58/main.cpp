#include <euler/lib/primes.h>

#include <iostream>

template <class T>
T ulam_diag_num(T n) {
    if ((n - 1) % 4 == 0) {
        auto k = (n - 1) / 2;

        return (k + 1) * (k + 1);
    }

    if ((n + 1) % 4 == 0) {
        auto k = (n + 1) / 2;

        return k * k + 1;
    }

    auto k = n / 2;

    return k * k + k + 1;
}

int main() {
    size_t p = 0;

    for (size_t i = 1; ; ++i) {
        auto u = ulam_diag_num(i);

        if (is_prime_stupid(u)) {
            ++p;
        }

        if (auto uu = (size_t)sqrt(u); uu * uu == u) {
            if (p) {
                if (i / p >= 10) {
                    std::cout << uu << std::endl;

                    return 0;
                }
            }
        }
    }
}
