#include <euler/lib/primes.h>

#include <map>
#include <iostream>

template <class T>
using primes_map_t = std::map<T, size_t>;

template <class T>
primes_map_t<T> to_primes_map(T t) noexcept {
    primes_map_t<T> res;

    for (auto p: to_primes(t)) {
        ++res[p];
    }

    return res;
}

template <class T>
T pov_int(T x, size_t n) noexcept {
    T res = x;

    while (n > 1) {
        res *= x;
        --n;
    }

    return res;
}

int main() {
    primes_map_t<unsigned> res;

    for (unsigned i = 2; i < 20; ++i) {
        auto pm = to_primes_map(i);

        for (auto it = pm.begin(); it != pm.end(); ++it) {
            auto& r = res[it->first];

            r = std::max(r, it->second);
        }
    }

    unsigned mul = 1;

    for (auto it = res.begin(); it != res.end(); ++it) {
        std::cout << it->first << " " << it->second << std::endl;
        mul *= pov_int(it->first, it->second);
    }

    std::cout << mul << std::endl;
}
