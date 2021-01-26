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

template <class T, class C>
C prepend_el(T t, C c) {
    C r;

    r.push_back(t);
    r.insert(r.end(), c.begin(), c.end());

    return r;
}
