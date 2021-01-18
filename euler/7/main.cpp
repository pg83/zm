#include <iostream>

template <class T>
bool is_prime_stupid(T t) {
    T x = 2;

    while (x * x <= t) {
        if (t % x == 0) {
            return false;
        }

        ++x;
    }

    return true;
}

int main() {
    unsigned x = 2;
    unsigned n = 0;

    while (true) {
        if (is_prime_stupid(x)) {
            ++n;

            if (n == 10001) {
                break;
            }
        }

        ++x;
    }

    std::cout << x << std::endl;
}
