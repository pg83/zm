#include <euler/lib/euler.h>

int main() {
    auto calc = memoized([](auto& calc, int n, int maxv) -> int {
        if (n < 0) {
            return 0;
        }

        if (n == 0) {
            return 1;
        }

        if (n == 1) {
            return 0;
        }

        int res = 0;

        for (int x = 2; x <= maxv; ++x) {
            if (is_prime_stupid(x)) {
                res += calc(n - x, x);
            }
        }

        return res;
    });

    for (int i = 0; ; ++i) {
        if (calc(i, i) > 5000) {
            std::cout << i << std::endl;

            break;
        }
    }
}
