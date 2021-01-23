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

static bool check(int n) {
    std::set<int> tmp;

    do {
        tmp.insert(n);
        n = sum_fac(n);
    } while (tmp.find(n) == tmp.end());

    return tmp.size() == 60;
}

int main() {
    size_t cnt = 0;

    for (int i = 0; i < 1000000; ++i) {
        if (check(i)) {
            ++cnt;
        }
    }

    std::cout << cnt << std::endl;
}
