#include <euler/lib/euler.h>

int main() {
    std::string tmp;

    for (int i = 0; tmp.length() < 2000000; ++i) {
        tmp += std::to_string(i);
    }

    auto c = [&] (size_t n) -> int {
        return tmp[n] - '0';
    };

    std::cout << c(1) * c(10) * c(100) * c(1000) * c(10000) * c(100000) * c(1000000) << std::endl;
}
