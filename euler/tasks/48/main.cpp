#include <euler/lib/euler.h>

int main() {
    bigint_t res;

    for (int i = 1; i <= 1000; ++i) {
        res += pow_int(bigint_t(i), i);
    }

    auto str = res.to_string();

    std::cout << str.substr(str.length() - 10) << std::endl;
}
