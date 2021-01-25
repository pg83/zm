#include <euler/lib/euler.h>

int main() {
    auto cb = partition_counter<bigint_t>();
    auto zr = bigint_t();
    auto md = bigint_t(1000000);

    for (int i = 0; ; ++i) {
        auto cnt = cb(i);

        if (cnt % md == zr) {
            std::cout << i << std::endl;

            break;
        }
    }
}
