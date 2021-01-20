#pragma once

#include <cstddef>

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
