#pragma once

#include "ratio.h"
#include "defer.h"
#include "any_iter.h"

template <class T>
auto farey_sequence(T n) {
    return any_sequence([a = T(0), b = T(1), c = T(1), d = T(n), n]() mutable {
        if (a > b) {
            throw stop_iteration_t();
        }

        defer {
            auto k = (n + b) / d;

            auto a1 = c;
            auto b1 = d;
            auto c1 = k * c - a;
            auto d1 = k * d - b;

            a = a1;
            b = b1;
            c = c1;
            d = d1;
        };

        return ratio_t(a, b);
    });
}
