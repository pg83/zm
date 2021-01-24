#pragma once

#include <algorithm>

template <class C>
C reversed(C c) {
    std::reverse(c.begin(), c.end());

    return c;
}

template <class C>
C sorted(C c) {
    std::sort(c.begin(), c.end());

    return c;
}

template <class C>
bool is_palindrom(const C& c) {
    return c == reversed(c);
}
