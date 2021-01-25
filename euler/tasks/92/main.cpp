#include <euler/lib/euler.h>

static int next(int n) noexcept {
    int res = 0;

    while (n) {
        auto d = n % 10;

        res += d * d;
        n /= 10;
    }

    return res;
}

static bool check(int n) noexcept {
    while (true) {
        n = next(n);

        if (n == 1) {
            return false;
        }

        if (n == 89) {
            return true;
        }
    }
}

int main() {
    int res = 0;

    for (int i = 1; i < 10000000; ++i) {
        if (check(i)) {
            ++res;
        }
    }

    std::cout << res << std::endl;
}
