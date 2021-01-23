#pragma once

#include <tp/libs/memo/include/memo.hpp>

template <class F>
auto memoized(F&& f) {
    return memo::recursive_memoize(std::forward<F>(f));
}
