#include <euler/lib/euler.h>

int main() {
    auto calc = memoized([&](auto& calc, int n) -> std::vector<std::vector<int>> {
        if (n == 1) {
            return {{1}};
        }

        std::vector<std::vector<int>> r;

        for (auto i = 2; i <= n; ++i) {
            if (n % i == 0) {
                for (const auto& s : calc(n / i)) {
                    if (i >= s.front()) {
                        r.push_back(prepend_el(i, s));
                    }
                }
            }
        }

        return r;
    });

    std::map<int, int> klasses;

    auto klass_of = [&](int n) {
        for (const auto& sol : calc(n)) {
            auto klass = n - std::accumulate(sol.begin(), sol.end(), 0) /*+1*/ + sol.size() /*+1*/;

            if (klass > 0) {
                if (klasses.find(klass) == klasses.end()) {
                    klasses[klass] = n;
                } else {
                    klasses[klass] = std::min(n, klasses[klass]);
                }
            }
        }
    };

    for (auto i = 1; i <= 24000; ++i) {
        klass_of(i);
    }

    std::set<int> res;

    for (int i = 2; i <= 12000; ++i) {
        res.insert(klasses[i]);
    }

    std::cout << std::accumulate(res.begin(), res.end(), 0) << std::endl;
}
