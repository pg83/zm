#include <euler/lib/euler.h>

static int count_primes(int a, int b) {
    int n = 0;

    while (is_prime_stupid(n * n + a * n + b)) {
        ++n;
    }

    return n;
}

int main() {
    int mab = 0;
    int mcp = 0;

    for (int a = -999; a <= 999; ++a) {
        for (int b = -1000; b <= 1000; ++b) {
            auto cp = count_primes(a, b);

            if (cp > mcp) {
                mcp = cp;
                mab = a * b;
            }
        }
    }

    std::cout << mab << std::endl;
}
