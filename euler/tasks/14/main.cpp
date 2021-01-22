#include <euler/lib/euler.h>

static size_t collatz_len(unsigned n) {
    if (n == 1) {
        return 1;
    }

    if (n % 2 == 0) {
        return 1 + collatz_len(n / 2);
    }

    return 1 + collatz_len(3 * n + 1);
}

int main() {
    std::cout << collatz_len(13) << std::endl;
    size_t cl = 0;
    unsigned v = 0;

    for (unsigned i = 1; i < 1000000; ++i) {
        auto l = collatz_len(i);

        if (l > cl) {
            cl = l;
            v = i;

            std::cout << v << " " << cl << std::endl;
        }
    }
}
