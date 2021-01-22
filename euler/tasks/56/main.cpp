#include <euler/lib/bigint.h>
#include <euler/lib/num.h>

#include <iostream>

static size_t dig_sum(const std::string& s) noexcept {
    size_t res = 0;

    for (auto ch : s) {
        res += ch - '0';
    }

    return res;
}

int main() {
    size_t maxs = 0;

    for (uint a = 1; a < 100; ++a) {
        for (uint b = 1; b < 100; ++b) {
            auto sum = dig_sum(pow_int(bigint_t(a), b).to_string());

            if (sum > maxs) {
                maxs = sum;

                std::cout << maxs << std::endl;
            }
        }
    }
}
