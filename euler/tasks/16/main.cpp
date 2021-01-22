#include <euler/lib/bigint.h>
#include <euler/lib/num.h>

#include <iostream>

int main() {
    std::cout << pow_int(bigint_t(2), 1000).dig_sum() << std::endl;
}
