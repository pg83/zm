#include <euler/lib/euler.h>

static const int facs[] = {
    factorial(0),
    factorial(1),
    factorial(2),
    factorial(3),
    factorial(4),
    factorial(5),
    factorial(6),
    factorial(7),
    factorial(8),
    factorial(9),
};

static int sum_fac(int n) noexcept {
    int res = 0;

    while (n) {
        res += facs[n % 10];
        n /= 10;
    }

    return res;
}

int main() {
    ui64 res = 0;

    for (int i = 3; i < 100000; ++i) {
        if (sum_fac(i) == i) {
            res += i;

            std::cout << i << std::endl;
        }
    }

    std::cout << res << std::endl;
}
