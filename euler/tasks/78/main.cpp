#include <euler/lib/euler.h>

int main() {
    auto cb = partition_counter<bigint_t>();

    for (int i = 0; ; ++i) {
        auto cnt = cb(i);

        if (cnt % 1000000 == int(0)) {
            std::cout << i << std::endl;

            break;
        }
    }
}
