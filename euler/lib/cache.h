#pragma once

#include <unordered_map>
#include <functional>

template <class X, class R>
struct cacher1_t {
    template <class F>
    cacher1_t(F&& ff) {
        f = [ff, this] (X x) -> const R& {
            auto& cc = c;

            if (cc.find(x) == cc.end()) {
                cc[x] = ff(x, *this);
            }

            return cc[x];
        };
    }

    const R& operator()(X x) {
        return f(x);
    }

    std::unordered_map<X, R> c;
    std::function<const R& (X)> f;
};

template <class X, class Y, class R>
struct cacher2_t {
    template <class F>
    cacher2_t(F&& ff) {
        f = [ff, this] (X x, Y y) -> const R& {
            auto& cc = c[y];

            if (cc.find(x) == cc.end()) {
                cc[x] = ff(x, y, *this);
            }

            return cc[x];
        };
    }

    const R& operator()(X x, Y y) {
        return f(x, y);
    }

    std::unordered_map<Y, std::unordered_map<X, R>> c;
    std::function<const R& (X, Y)> f;
};
