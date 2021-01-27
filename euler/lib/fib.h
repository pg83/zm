#pragma once

#include "any_iter.h"

template <class T>
auto fibo_sequence() {
    return any_sequence([a = T(1), b = T(1)]() mutable {
        auto t = a;

        a = b;
        b = b + t;

        return t;
    });
}
