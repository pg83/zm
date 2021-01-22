#include <euler/lib/euler.h>

template <class T>
bool is_amicable(T a) {
    auto b = proper_divisors_sum(a);

    return b != a && proper_divisors_sum(b) == a;
}

int main() {
    unsigned res = 0;

    for (unsigned x = 1; x < 10000; ++x) {
        if (is_amicable(x)) {
            res += x;
        }
    }

    std::cout << res << std::endl;
}
