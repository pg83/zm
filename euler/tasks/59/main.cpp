#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

static const int data[] = {
    #include "p059_cipher.txt"
};

using cy_key_t = std::vector<int>;

static bool decode(const cy_key_t& key, std::string& r) {
    auto c = 0;

    for (auto i : data) {
        auto v = key[c % key.size()] ^ i;

        if (v < 31) {
            return false;
        }

        if (v > 122) {
            return false;
        }

        r += (char)v;
        c += 1;
    }

    return true;
}

int main() {
    for (auto i = 97; i <= 122; ++i) {
        for (auto j = 97; j <= 122; ++j) {
            for (auto k = 97; k <= 122; ++k) {
                auto key = cy_key_t({i, j, k});

                if (std::string msg; decode(key, msg)) {
                    if (std::count(msg.begin(), msg.end(), 'a') > 50) {
                        std::cout << std::accumulate(msg.begin(), msg.end(), 0) << std::endl;
                    }
                }
            }
        }
    }
}
