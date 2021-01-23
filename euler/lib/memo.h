#pragma once

#include <unordered_map>
#include <functional>

template <class X, class R, class F>
struct memo1_t {
    memo1_t(const F& ff)
        : f(ff)
    {
    }

    const R& operator()(X x) {
        auto& cc = c;

        if (cc.find(x) == cc.end()) {
            cc[x] = f(*this, x);
        }

        return cc[x];
    }

    std::unordered_map<X, R> c;
    F f;
};

template <class X, class R, class F>
auto memoized1(F&& f) {
    return memo1_t<X, R, F>(std::forward<F>(f));
}

template <class X, class Y, class R, class F>
struct memo2_t {
    memo2_t(const F& ff)
        : f(ff)
    {
    }

    const R& operator()(X x, Y y) {
        auto& cc = c[y];

        if (cc.find(x) == cc.end()) {
            cc[x] = f(*this, x, y);
        }

        return cc[x];
    }

    std::unordered_map<Y, std::unordered_map<X, R>> c;
    F f;
};

template <class X, class Y, class R, class F>
auto memoized2(F&& f) {
    return memo2_t<X, Y, R, F>(std::forward<F>(f));
}
