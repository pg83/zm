#pragma once

#include "types.h"
#include "cache.h"

template <class R>
struct cnk_t: public cacher2_t<uint, uint, R> {
    cnk_t()
        : cacher2_t<uint, uint, R>([](uint n, uint k, auto& cnk) -> R {
            if (k == 0) {
                return 1;
            }

            if (n == k) {
                return 1;
            }

            return cnk(n - 1, k - 1) + cnk(n - 1, k);
        })
    {
    }
};
