#include <euler/lib/primes.h>

#include <iostream>

template <class T>
int prime_count(T t) {
    T r = T(1);
    int x = 0;

    for (auto p : to_primes(t)) {
        if (r % p == 0) {
        } else {
            r *= p;
            ++x;
        }
    }

    return x;
}

int main() {
    for (int res = 1; ; ++res) {
        auto a = res;
        auto b = a + 1;
        auto c = a + 2;
        auto d = a + 3;

        if (prime_count(a) == 4) {
            if (prime_count(b) == 4) {
                if (prime_count(c) == 4) {
                    if (prime_count(d) == 4) {
                        std::cout << res << std::endl;

                        return 0;
                    }
                }
            }
        }
    }
}
