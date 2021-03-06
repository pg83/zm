#pragma once

#include "types.h"
#include "memo.h"
#include "bigint.h"
#include "any_iter.h"
#include "defer.h"

#include <vector>
#include <algorithm>

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
    return memoized([zero = T(int(0)), one = T(int(1))](auto& pc, long n) -> T {
        if (n < 0) {
            return zero;
        }

        if (n == 0) {
            return one;
        }

        T res = zero;
        long k = 1;

        while (true) {
            auto p = pc(n - (k * (3 * k - 1)) / 2);

            if (p == zero) {
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
}

// https://msdn.microsoft.com/en-us/library/aa289166.aspx
template <class V>
void first_combination(int k, V& v) {
    for (int i = 0; i < k; ++i) {
        v.push_back(i);
    }
}

inline auto first_combination(int k) {
    std::vector<int> tmp;

    first_combination(k, tmp);

    return tmp;
}

template <class V>
bool next_combination(int n, V& ans) {
    if (ans.empty()) {
        return false;
    }

    auto k = (int)ans.size();

    if (ans[0] == n - k) {
        return false;
    }

    auto i = k - 1;

    while (i > 0 && ans[i] == n - k + i) {
        i -= 1;
    }

    ans[i] += 1;

    for (int j = i; j < k - 1; ++j) {
        ans[j + 1] = ans[j] + 1;
    }

    return true;
}

inline auto combination_sequence(int k, int n) {
    return any_sequence([n, tmp = first_combination(k), at_end = false]() mutable {
        if (at_end) {
            throw stop_iteration_t();
        }

        Z_DEFER {
            at_end = !next_combination(n, tmp);
        };

        return tmp;
    });
}

template <class V>
inline auto permutation_sequence(V v) {
    return any_sequence([v, at_end=false]() mutable {
        if (at_end) {
            throw stop_iteration_t();
        }

        Z_DEFER {
            at_end = !std::next_permutation(v.begin(), v.end());
        };

        return v;
    });
}

template <class S, class F>
auto transform_sequence(S s, F f) {
    return any_sequence([b = s.begin(), e = s.end(), f, s]() mutable {
        if (b == e) {
            throw stop_iteration_t();
        }

        Z_DEFER {
            ++b;
        };

        return f(*b);
    });
}
