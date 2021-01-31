#pragma once

#include <libs/platform/types.h>

#include <ostream>

using ui128 = __uint128_t;
using i128 = __int128_t;

void out(std::ostream& o, ui128 v);
void out(std::ostream& o, i128 v);

inline std::ostream& operator<<(std::ostream& o, ui128 v) {
    out(o, v);

    return o;
}

inline std::ostream& operator<<(std::ostream& o, i128 v) {
    out(o, v);

    return o;
}
