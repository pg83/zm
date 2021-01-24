#pragma once

#include "types.h"

#include <deque>
#include <map>

template <class T>
using primes_t = std::deque<T>;

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
primes_t<T> to_primes(T x) noexcept {
    primes_t<T> c;

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

template <class T>
uint uniq_prime_count(T t) {
    T r = T(1);
    uint x = 0;

    for (auto p : to_primes(t)) {
        if (r % p == 0) {
        } else {
            r *= p;
            ++x;
        }
    }

    return x;
}

template <class T>
T euler_totient(T n) {
    T r = 1;

    for (const auto& [p, i] : to_primes_map(n)) {
        r *= pow_int(p, i - 1) * (p - 1);
    }

    return r;
}

template <class T>
T gcd(T a, T b) {
    while (b) {
        auto c = a % b;

        a = b;
        b = c;
    }

    return a;
}

template <class T>
T gcd(T a, T b, T c) {
    return gcd(a, gcd(b, c));
}

template <class T>
bool co_prime(T l, T r) {
    return gcd(l, r) == 1;
}
