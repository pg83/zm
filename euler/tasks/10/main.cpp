#include <euler/lib/euler.h>

int main() {
    size_t sum = 0;

    for (size_t i = 2; i < 2000000; ++i) {
        if (is_prime_stupid(i)) {
            sum += i;
        }
    }

    std::cout << sum << std::endl;
}
