#include <set>
#include <vector>
#include <numeric>
#include <iostream>
#include <initializer_list>

static bool is_pand(int a, int b, int c) noexcept {
    std::vector<int> digits;

    for (auto n : {a, b, c}) {
        while (n) {
            auto d = n % 10;

            if (d == 0) {
                return false;
            }

            digits.push_back(d);
            n /= 10;
        }
    }

    return digits.size() == 9 && std::set<int>(digits.begin(), digits.end()).size() == 9;
}

int main() {
    std::set<int> res;

    for (int a = 1; a < 1000000; ++a) {
        for (int b = 1; b < 1000000 / a; ++b) {
            if (is_pand(a, b, a * b)) {
                res.insert(a * b);
            }
        }
    }

    std::cout << std::accumulate(res.begin(), res.end(), 0) << std::endl;
}
