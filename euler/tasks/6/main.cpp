#include <euler/lib/euler.h>

int main() {
    unsigned res = 0;

    for (unsigned i = 1; i <= 100; ++i) {
        for (unsigned j = 1; j <= 100; ++j) {
            if (i != j) {
                res += i * j;
            }
        }
    }

    std::cout << res << std::endl;
}
