#include <euler/lib/euler.h>

int main() {
    auto primes = to_primes(600851475143ull);

    std::cout << *std::max_element(primes.begin(), primes.end()) << std::endl;
}
