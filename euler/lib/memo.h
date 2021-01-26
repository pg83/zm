#pragma once

#include <tp/libs/memo/include/memo.hpp>

template <class F>
auto memoized(F&& f) {
    return memo::recursive_memoize(std::forward<F>(f));
}

template <class F>
struct recursive_t {
    template <typename... Args>
    decltype(auto) operator()(Args... args) {
        return f(*this, std::forward<Args>(args)...);
    }

    F f;
};

template <class F>
recursive_t<F> recursive(F&& f) {
    return {std::forward<F>(f)};
}
