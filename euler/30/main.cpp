#include <euler/lib/num.h>

#include <iostream>

static int sum5(int n) noexcept {
    int res = 0;

    while (n) {
        res += pow_int(n % 10, 5);
        n /= 10;
    }

    return res;
}

int main() {
    int res = 0;

    for (int i = 2; i < 1000000; ++i) {
        if (sum5(i) == i) {
            res += i;
        }
    }

    std::cout << res << std::endl;
}
