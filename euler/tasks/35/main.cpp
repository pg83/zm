#include <euler/lib/num.h>
#include <euler/lib/primes.h>

#include <cstddef>
#include <iostream>

template <class T>
size_t num_digits(T n) noexcept {
    if (n == 0) {
        return 1;
    }

    size_t res = 0;

    while (n) {
        ++res;
        n /= 10;
    }

    return res;
}

static bool is_circular(int n) noexcept {
    auto d = num_digits(n);
    auto pd = pow_int(10, d - 1);

    for (uint i = 0; i < d; ++i) {
        n = (n % 10) * pd + n / 10;

        if (!is_prime_stupid(n)) {
            return false;
        }
    }

    return true;
}

int main() {
    size_t res = 0;

    for (int i = 2; i < 1000000; ++i) {
        if (is_circular(i)) {
            ++res;
        }
    }

    std::cout << res << std::endl;
}
