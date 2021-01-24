#pragma once

#include "types.h"
#include "memo.h"
#include "bigint.h"

template <class R>
auto cnk() {
    return memoized([](auto& cnk, uint n, uint k) -> R {
        if (k == 0) {
            return 1;
        }

        if (n == k) {
            return 1;
        }

        return cnk(n - 1, k - 1) + cnk(n - 1, k);
    });
}

using pq_t = std::pair<bigint_t, bigint_t>;

template <class F>
auto eval_pq(F&& cf) {
    return memoized([cf](auto& eval, int n) -> pq_t {
        if (n == -1) {
            return {1, 0};
        }

        if (n == -2) {
            return {0, 1};
        }

        auto pq1 = eval(n - 1);
        auto pq2 = eval(n - 2);

        auto a = cf((size_t)n);

        return {a * pq1.first + pq2.first, a * pq1.second + pq2.second};
    });
}

template <class T>
auto partition_counter() {
    auto pc = memoized ([](auto& pc, T n) -> T {
        if (n < 0) {
            return 0;
        }

        if (n == 0) {
            return 1;
        }

        T res = 0;
        int k = 1;

        while (true) {
            auto p = pc(n - (k * (3 * k - 1)) / 2);

            if (p == 0) {
                return res;
            }

            if ((k - 1) % 2 == 0) {
                res = res + p;
            } else {
                res = res - p;
            }

            if (k > 0) {
                k = -k;
            } else {
                k = -k + 1;
            }
        }
    });

    return pc;
}
