#include <euler/lib/bigint.h>
#include <euler/lib/num.h>

#include <iostream>

int main() {
    unsigned res = 0;

    for (auto ch : pow_int(bigint_t(2), 1000).to_string()) {
        res += ch - '0';
    }

    std::cout << res << std::endl;
}
