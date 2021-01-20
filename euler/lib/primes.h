#pragma once

#include <deque>
#include <map>

template <class T>
bool is_prime_stupid(T t) {
    if (t < 2) {
        return false;
    }

    T x = 2;

    while (x * x <= t) {
        if (t % x == 0) {
            return false;
        }

        ++x;
    }

    return true;
}

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

template <class T>
using primes_map_t = std::map<T, size_t>;

template <class T>
primes_map_t<T> to_primes_map(T t) noexcept {
    primes_map_t<T> res;

    for (auto p: to_primes(t)) {
        ++res[p];
    }

    return res;
}

template <class T>
size_t num_divisors(T t) noexcept {
    auto m = to_primes_map(t);
    size_t res = 1;

    for (auto it = m.begin(); it != m.end(); ++it) {
        res *= (1 + it->second);
    }

    return res;
}

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
