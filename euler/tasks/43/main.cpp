#include <euler/lib/num.h>

#include <vector>
#include <algorithm>
#include <iostream>
#include <cstddef>
#include <numeric>

static bool check(ui64 n) {
    for (auto div : {17, 13, 11, 7, 5, 3, 2}) {
        if ((n % 1000) % div != 0) {
            return false;
        }

        n /= 10;
    }

    return true;
}

int main() {
    ui64 res = 0;
    std::vector<int> tmp({0, 1, 2, 3, 4, 5, 6, 7, 8, 9});

    do {
        auto num = to_number<ui64>(tmp);

        if (check(num)) {
            res += num;

            std::cout << num << std::endl;
        }
    } while (std::next_permutation(tmp.begin(), tmp.end()));

    std::cout << res << std::endl;
}
