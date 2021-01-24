#include <euler/lib/euler.h>

static const int coins[] = {200, 100, 50, 20, 10, 5, 2, 1};

struct params_t {
    int n;
    const int* b;
    const int* e;

    int key() const noexcept {
        return std::accumulate(b, e, 0) * 10000 + n;
    }

    friend bool operator==(const params_t& l, const params_t& r) noexcept {
        return l.key() == r.key();
    }

    friend bool operator<(const params_t& l, const params_t& r) noexcept {
        return l.key() < r.key();
    }
};

int main() {
    auto calc = memoized([] (auto& calc, params_t p) -> int {
        if (p.n == 0) {
            return 1;
        }

        auto c = *p.b;

        if (c == 1) {
            return 1;
        }

        int res = 0;

        for (int j = 0; j <= p.n / c; ++j) {
            res += calc(params_t{p.n - j * c, p.b + 1, p.e});
        }

        return res;
    });

    std::cout << calc(params_t{200, coins, coins + std::size(coins)}) << std::endl;
}
