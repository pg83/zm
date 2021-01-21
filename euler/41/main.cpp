#include <euler/lib/primes.h>

#include <iostream>
#include <cstddef>
#include <numeric>
#include <vector>
#include <algorithm>

template <class C>
uint64_t to_number(const C& c) noexcept {
    uint64_t res = 0;

    for (auto d : c) {
        res = res * 10 + d;
    }

    return res;
}

int main() {
    std::vector<uint64_t> res;
    std::vector<int> d;

    d.push_back(1);

    for (int i = 2; i <= 9; ++i) {
        d.push_back(i);

        auto tmp = d;

        do {
            auto n = to_number(tmp);

            if (is_prime_stupid(n)) {
                res.push_back(n);
            }
        } while (std::next_permutation(tmp.begin(), tmp.end()));
    }

    std::sort(res.begin(), res.end());

    std::cout << res.back() << std::endl;
}
