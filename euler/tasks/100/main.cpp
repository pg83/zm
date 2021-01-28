#include <euler/lib/euler.h>

auto iter_solutions() {
    return any_sequence([x = bigint_t(41), y = bigint_t(29)]() mutable {
        while (true) {
            Z_DEFER {
                const auto x1 = 3 * x + 4 * y;
                const auto y1 = 2 * x + 3 * y;

                x = x1;
                y = y1;
            };

            if (x.is_odd() && y.is_odd()) {
                return std::make_pair((y + 1) / 2, (x + 1) / 2);
            }
        }
    });
}

int main() {
    auto N = pow_int(bigint_t(10), 12);

    for (auto [n, m] : iter_solutions()) {
        if (N < m) {
            std::cout << n << std::endl;

            break;
        }
    }
}
