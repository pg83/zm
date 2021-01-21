#include <euler/lib/algo.h>
#include <euler/lib/primes.h>

#include <map>
#include <vector>
#include <string>
#include <iostream>

int main() {
    std::map<std::string, std::vector<int>> eq;

    for (int n = 1000; n <= 9999; ++n) {
        if (is_prime_stupid(n)) {
            eq[sorted(std::to_string(n))].push_back(n);
        }
    }

    for (auto it : eq) {
        auto& v = it.second;

        if (v.size() < 3) {
            continue;
        }

        do {
            auto x = sorted(std::vector<int>(v.begin(), v.begin() + 3));

            if (x[1] - x[0] == x[2] - x[1]) {
                if (x[0] != 1487) {
                    std::cout << x[0] << x[1] << x[2] << std::endl;

                    return 0;
                }
            }
        } while (std::next_permutation(v.begin(), v.end()));
    }
}
