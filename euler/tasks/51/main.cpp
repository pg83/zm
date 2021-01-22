#include <euler/lib/primes.h>
#include <euler/lib/strutils.h>

#include <set>
#include <unordered_map>
#include <unordered_set>
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
    auto res = replace(k, '*', '0' + d);

    if (res[0] == '0') {
        return 0;
    }

    return from_string<int>(res);
}

int main() {
    std::unordered_set<std::string> keys;
    std::unordered_map<std::string, std::set<int>> res;

    for (int i = 1; i <= 200000; ++i) {
        for (int d = 0; d <= 9; ++d) {
            keys.insert(keyf(i, d));
        }
    }

    for (const auto& k : keys) {
        for (int d = 0; d <= 9; ++d) {
            auto kk = unkeyf(k, d);

            if (is_prime_stupid(kk)) {
                res[k].insert(kk);
            }
        }
    }

    for (auto& it : res) {
        auto& v = it.second;

        if (v.size() == 8) {
            std::cout << *v.begin() << std::endl;

            break;
        }
    }
}
