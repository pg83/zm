#include <euler/lib/num.h>
#include <euler/lib/bigint.h>

#include <set>
#include <iostream>

int main() {
    std::set<std::string> res;

    for (bigint_t a = 2; a <= 100; ++a) {
        for (int b = 2; b <= 100; ++b) {
            res.insert(pow_int(a, b).to_string());
        }
    }

    std::cout << res.size() << std::endl;
}
