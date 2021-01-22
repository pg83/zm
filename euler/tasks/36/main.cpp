#include <euler/lib/euler.h>

std::vector<int> to_bin(int n) {
    std::vector<int> res;

    while (n) {
        res.push_back(n % 2);
        n /= 2;
    }

    return res;
}

static bool check(int n) {
    if (n % 10 == 0) {
        return false;
    }

    if (n % 2 == 0) {
        return false;
    }

    if (!is_palindrom(std::to_string(n))) {
        return false;
    }

    if (!is_palindrom(to_bin(n))) {
        return false;
    }

    return true;
}

int main() {
    size_t res = 0;

    for (int i = 1; i < 1000000; ++i) {
        if (check(i)) {
            res += i;

            std::cout << i << std::endl;
        }
    }

    std::cout << res << std::endl;
}
