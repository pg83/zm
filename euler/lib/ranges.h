#pragma once

#include <range/v3/all.hpp>

namespace rs = ranges;
namespace rv = ranges::views;
namespace ra = ranges::actions;

inline auto sqr_fn() {
    return [](auto i) {
        return i * i;
    };
}
