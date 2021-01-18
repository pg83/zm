#pragma once

#include <cstddef>

template <class T>
T pov_int(T x, size_t n) noexcept {
    T res = T(1);

    while (n) {
        res *= x;
        --n;
    }

    return res;
}
