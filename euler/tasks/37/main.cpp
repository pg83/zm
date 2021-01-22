#include <euler/lib/euler.h>

template <class T>
T rotate10(T n) noexcept {
    T res = 0;

    while (n) {
        res = res * 10 + n % 10;
        n /= 10;
    }

    return res;
}

static bool check(int n) {
    auto r = rotate10(n);

    while (n) {
        if (!is_prime_stupid(n)) {
            return false;
        }

        n /= 10;
    }

    while (r) {
        if (!is_prime_stupid(rotate10(r))) {
            return false;
        }

        r /= 10;
    }

    return true;
}

int main() {
    int res = 0;

    for (int c = 0, i = 10; c < 11; ++i) {
        if (check(i)) {
            ++c;
            res += i;

            std::cout << i << std::endl;
        }
    }

    std::cout << res << std::endl;
}
