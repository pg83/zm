#include <euler/lib/euler.h>

static const bigint_t mult = pow_int(bigint_t(10), 220);

static int sum_str(const std::string& s) noexcept {
    int res = 0;

    for (size_t i = 0; i < 100; ++i) {
        res += s[i] - '0';
    }

    return res;
}

static int ss(const bigint_t& v) {
    return sum_str((v * mult).sqrt().to_string());
}

int main() {
    std::set<int> powers;

    for (int i = 1; i < 100; ++i) {
        powers.insert(i * i);
    }

    int res = 0;

    for (int i = 1; i <= 100; ++i) {
        if (powers.find(i) == powers.end()) {
            res += ss(i);
        }
    }

    std::cout << res << std::endl;
}
