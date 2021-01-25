#pragma once

#include "preproc.h"

#include <utility>

template <class F>
struct defer_t {
    F f;

    defer_t(const F& ff)
        : f(ff)
    {
    }

    ~defer_t() {
        f();
    }
};

struct defer_maker_t {
    template <class F>
    defer_t<F> operator|(F&& f) {
        return std::forward<F>(f);
    }
};

#define defer [[maybe_unused]] const auto& Z_GENERATE_UNIQUE_ID(defer) = defer_maker_t() | [&]()
