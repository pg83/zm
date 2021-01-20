#include <euler/lib/num.h>
#include <euler/lib/bigint.h>

#include <set>
#include <iostream>

int main() {
    std::set<bigint_t> res;

    for (bigint_t a = 2, maxa = 100; a <= maxa; ++a) {
        for (int b = 2; b <= 100; ++b) {
            res.insert(pow_int(a, b));
        }
    }

    std::cout << res.size() << std::endl;
}
