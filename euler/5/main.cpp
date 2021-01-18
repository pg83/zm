#include <euler/lib/primes.h>
#include <euler/lib/num.h>

#include <iostream>

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
