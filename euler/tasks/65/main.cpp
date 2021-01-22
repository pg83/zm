#include <euler/lib/euler.h>

static int e_frac(size_t nn) noexcept {
    auto n = nn + 1;

    if (n == 1) {
        return 2;
    }

    if (n % 3 == 0) {
        return (2 * n) / 3;
    }

    return 1;
}

int main() {
    std::cout << eval_pq_t(e_frac)(99).first.digit_sum() << std::endl;
}
