#include <euler/lib/fib.h>

#include <iostream>
#include <cstdint>

int main() {
    unsigned sum = 0;

    for (auto x : fibo_seq_t<unsigned>()) {
        if (x > 4000000) {
            break;
        }

        if (x % 2 == 0) {
            sum += x;
        }
    }

    std::cout << sum << std::endl;
}
