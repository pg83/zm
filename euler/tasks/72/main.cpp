#include <euler/lib/euler.h>

int main() {
    bigint_t r;

    for (int d = 2; d <= 1000000; ++d) {
        r += euler_totient(d);
    }

    std::cout << r << std::endl;
}
