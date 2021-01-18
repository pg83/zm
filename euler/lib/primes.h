#include <deque>

template <class T, class C>
void to_primes(T x, C& c) noexcept {
    T p = 2;

    while (p * p <= x) {
        if (x % p == 0) {
            c.push_back(p);
            to_primes(x / p, c);

            return;
        }

        ++p;
    }

    c.push_back(x);
}

template <class T>
std::deque<T> to_primes(T x) noexcept {
    std::deque<T> c;
    to_primes(x, c);

    return c;
}
