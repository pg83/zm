#include <euler/lib/euler.h>

int main() {
    unsigned tn = 0;
    unsigned n = 0;

    while (true) {
        n += 1;
        tn += n;

        auto nd = num_divisors(tn);

        std::cout << n << " " << tn << " " << nd << std::endl;

        if (nd >= 500) {
            break;
        }
    }

    std::cout << tn << std::endl;
}
