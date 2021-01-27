#include <euler/lib/euler.h>

static bigint_t pell_fund_sol(int d) {
    auto ev = eval_qir(d);

    for (long i = 0; ; ++i) {
        const auto& [x, y] = ev(i);

        if (x * x == d * y * y + 1) {
            return x;
        }
    }

    return 0l;
}

int main() {
    auto sq = rv::iota(1, 1001) | rv::transform(sqr_fn()) | rs::to<std::set>;

    bigint_t x;
    long xd = 0;

    for (long d = 2; d <= 1000; ++d) {
        if (sq.find(d) == sq.end()) {
            auto sol = pell_fund_sol(d);

            if (sol > x) {
                x = sol;
                xd = d;
            }
        }
    }

    std::cout << xd << std::endl;
}
