#include <euler/lib/primes.h>
#include <euler/lib/num.h>

#include <iostream>
#include <cstddef>
#include <numeric>
#include <vector>
#include <algorithm>

int main() {
    std::vector<uint64_t> res;
    std::vector<int> d;

    d.push_back(1);

    for (int i = 2; i <= 9; ++i) {
        d.push_back(i);

        auto tmp = d;

        do {
            auto n = to_number<uint64_t>(tmp);

            if (is_prime_stupid(n)) {
                res.push_back(n);
            }
        } while (std::next_permutation(tmp.begin(), tmp.end()));
    }

    std::sort(res.begin(), res.end());

    std::cout << res.back() << std::endl;
}
