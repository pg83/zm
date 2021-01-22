#include <euler/lib/euler.h>

int main() {
    unsigned x = 2;
    unsigned n = 0;

    while (true) {
        if (is_prime_stupid(x)) {
            ++n;

            if (n == 10001) {
                break;
            }
        }

        ++x;
    }

    std::cout << x << std::endl;
}
