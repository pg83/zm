#include <euler/lib/euler.h>

int main() {
    auto pc = partition_counter<bigint_t>();

    std::cout << pc(100) - 1 << std::endl;
}
