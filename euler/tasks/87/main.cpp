#include <euler/lib/euler.h>

int main() {
    std::vector<ui64> v1;

    for (ui64 t = 1; t < 10000; ++t) {
        if (is_prime_stupid(t)) {
            v1.push_back(t * t);
        }
    }

    std::vector<ui64> v2;

    for (ui64 t = 1; t < 1000; ++t) {
        if (is_prime_stupid(t)) {
            v2.push_back(t * t * t);
        }
    }

    std::vector<ui64> v3;

    for (ui64 t = 1; t < 100; ++t) {
        if (is_prime_stupid(t)) {
            v3.push_back(t * t * t * t);
        }
    }

    std::set<ui64> res;

    for (auto i : v1) {
        for (auto j : v2) {
            for (auto k : v3) {
                res.insert(i + j + k);
            }
        }
    }

    size_t r = 0;

    for (auto x : res) {
        if (x < 50000000) {
            r += 1;
        }
    }

    std::cout << r << std::endl;
}
