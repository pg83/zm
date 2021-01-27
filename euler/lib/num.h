#pragma once

#include "types.h"

#include <cmath>

template <class T>
T pow_int(T a, size_t pow) noexcept {
    T res = T(1);
    T cur = a;

    while (pow > 0) {
        if (pow % 2 == 0) {
            cur = cur * cur;
            pow /= 2;
        } else {
            res = res * cur;
            pow -= 1;
        }
    }

    return res;
}

template <class T>
T sqrt_int(T v) noexcept {
    return (T)std::sqrt(v);
}

template <class T>
T sqr(T i) {
    return i * i;
}

template <class T>
T factorial(T n) {
    if (n < 2) {
        return 1;
    }

    T res = T(1);

    for (T t = 2; t <= n; ++t) {
        res *= t;
    }

    return res;
}

template <class T, class C>
T to_number(const C& c) noexcept {
    T res = 0;

    for (auto d : c) {
        res = res * 10 + d;
    }

    return res;
}
