#include <euler/lib/euler.h>

static bigint_t pell_fund_sol(int d) {
    auto cf = qir_t<long>::root_of(d).cont_fraction();

    auto ev = eval_pq_t([&](size_t n) -> long {
        if (n == 0) {
            return cf[0];
        }

        return cf[1 + ((n - 1) % (cf.size() - 1))];
    });

    for (long i = 0; i <= 1000000; ++i) {
        auto pq = ev(i);
        auto x = pq.first;
        auto y = pq.second;

        if (x * x == d * y * y + 1) {
            return x;
        }
    }

    return 0l;
}

int main() {
    bigint_t x;
    long xd = 0;
    std::set<long> sq;

    for (long i = 1; i <= 1000; ++i) {
        sq.insert(i * i);
    }

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
