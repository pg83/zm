#include <iostream>

template <class T>
T proper_divisors_sum(T x) {
    T res = 0;

    for (T d = 2, max = sqrt(x); d <= max; ++d) {
        if (x % d == 0) {
            T dd = x / d;

            if (d == dd) {
                res += d;
            } else {
                res += d + dd;
            }
        }
    }

    return res + 1;
}

template <class T>
bool is_amicable(T a) {
    auto b = proper_divisors_sum(a);

    return b != a && proper_divisors_sum(b) == a;
}

int main() {
    std::cout << proper_divisors_sum(220) << " " << proper_divisors_sum(284) << std::endl;
    std::cout << is_amicable(220) << std::endl;

    unsigned res = 0;

    for (unsigned x = 1; x < 10000; ++x) {
        if (is_amicable(x)) {
            res += x;
        }
    }

    std::cout << res << std::endl;
}
