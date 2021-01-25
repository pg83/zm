#include <euler/lib/euler.h>

int main() {
    using int_t = mod_int_t<ui128, 10000000000>;

    std::cout << int_t(28433) * pow_int(int_t(2), 7830457) + int_t(1) << std::endl;
}
