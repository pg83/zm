#include <euler/lib/primes.h>
#include <euler/lib/strutils.h>

#include <set>
#include <unordered_map>
#include <vector>
#include <string>
#include <iostream>

static std::string replace(std::string s, char f, char t) {
    for (auto& ch : s) {
        if (ch == f) {
            ch = t;
        }
    }

    return s;
}

static std::string keyf(int n, int d) {
    return replace(std::to_string(n), '0' + d, '*');
}

static int unkeyf(const std::string& k, int d) {
    return from_string<int>(replace(k, '*', '0' + d));
}

int main() {
    std::unordered_map<std::string, std::set<int>> res;

    for (int i = 1; i <= 1000000; ++i) {
        for (int d = 0; d <= 9; ++d) {
            auto k = keyf(i, d);

            for (int s = 0; s <= 9; ++s) {
                auto kk = unkeyf(k, s);

                if (is_prime_stupid(kk)) {
                    res[k].insert(kk);
                }
            }
        }
    }

    for (auto& it : res) {
        auto& v = it.second;

        if (v.size() == 8) {
            std::cout << it.first << " " << *v.begin() << std::endl;
        }
    }
}
