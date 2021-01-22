#pragma once

#include "types.h"
#include "cache.h"
#include "bigint.h"

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

using pq_t = std::pair<bigint_t, bigint_t>;

template <class T>
struct eval_pq_t: public cacher1_t<T, pq_t> {
    template <class F>
    eval_pq_t(F&& cf)
        : cacher1_t<T, pq_t>([this, &cf](T n, auto& eval) -> pq_t {
            if (n == -1) {
                return {b1, b0};
            }

            if (n == -2) {
                return {b0, b1};
            }

            auto pq1 = eval(n - 1);
            auto pq2 = eval(n - 2);

            auto a = cf(n);

            return {a * pq1.first + pq2.first, a * pq1.second + pq2.second};
        })
    {
    }

    const bigint_t b0 = long(0);
    const bigint_t b1 = long(1);
};
