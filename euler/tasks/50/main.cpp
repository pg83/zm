#include <euler/lib/primes.h>

#include <vector>
#include <iostream>

int main() {
    long s = 0;
    std::vector<ulong> sums;

    for (ulong i = 0; i < 100000; ++i) {
        if (is_prime_stupid(i)) {
            s += i;
            sums.push_back(s);
        }
    }

    ulong maxd = 0;
    ulong maxp = 0;

    for (size_t i = 0; i < sums.size(); ++i) {
        for (size_t j = 0; j < sums.size(); ++j) {
            if (i > j) {
                auto ip = sums[i];
                auto jp = sums[j];

                auto d = i - j;
                auto p = ip - jp;

                if (p < 1000000) {
                    if (d > maxd) {
                        if (is_prime_stupid(p)) {
                            maxd = d;
                            maxp = p;

                            std::cout << maxd << " " << maxp << std::endl;
                        }
                    }
                }
            }
        }
    }

    std::cout << maxp << std::endl;
}
