#include <euler/lib/euler.h>

int main() {
    bigint_t res;

    auto check = [](long a, long b) {
        auto d = 4 * a * a - b * b;
        auto s = sqrt_int(d);

        return (2 * a > b) && (s * s == d) && ((b * s) % 4 == 0);
    };

    for (auto i: rv::iota(1, 350000000)) {
        if (check(i - 1, i)) {
            res = res + (3 * i - 2);
        }

        if (check(i + 1, i)) {
            res = res + (3 * i + 2);
        }
    }

    std::cout << res << std::endl;
}
