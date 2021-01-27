#include <euler/lib/euler.h>

static const bigint_t mult = pow_int(bigint_t(10), 220);

static int sum_str(const std::string& s) noexcept {
    return digit_sum(s.substr(0, 100));
}

static int ss(const bigint_t& v) {
    return sum_str((v * mult).sqrt().to_string());
}

int main() {
    auto powers = rv::iota(0, 100) | rv::transform(sqr_fn()) | rs::to<std::set>;

    int res = 0;

    for (int i = 1; i <= 100; ++i) {
        if (powers.find(i) == powers.end()) {
            res += ss(i);
        }
    }

    std::cout << res << std::endl;
}
