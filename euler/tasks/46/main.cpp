#include <euler/lib/primes.h>

#include <unordered_set>
#include <iostream>

int main() {
    std::unordered_set<int> res;
    auto n = 1000000;

    for (auto i = 0; i < n; ++i) {
        if (is_prime_stupid(i)) {
            auto x = 0;
            auto j = 1;

            do {
                x = i + 2 * j * j;
                ++j;
                res.insert(x);
            } while (x <= n);
        }
    }

    for (auto i = 1; i < n / 2; ++i) {
        auto j = i * 2 + 1;

        if (is_prime_stupid(j)) {
            continue;
        }

        if (res.find(j) == res.end()) {
            std::cout << j << std::endl;

            break;
        }
    }
}
