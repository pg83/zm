#include <euler/lib/euler.h>

int main() {
    auto bn = 0;
    auto rn = 0.0;

    for (int i = 2; i <= 1000000; ++i) {
        auto res = euler_totient(i);
        auto rat = double(i) / double(res);

        if (rat >= rn) {
            rn = rat;
            bn = i;

            std::cout << bn << " " << rn << std::endl;
        }
    }

    std::cout << bn << std::endl;
}
