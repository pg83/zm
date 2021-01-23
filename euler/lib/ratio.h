#pragma once

#include "num.h"

#include <ostream>

// ratio
template <class T>
struct ratio_t {
    T a;
    T b;

    ratio_t(T p, T q)
        : a(p)
        , b(q)
    {
    }

    ratio_t(T p)
        : a(p)
        , b(1)
    {
    }

    //cmp
    friend bool operator<(const ratio_t& l, const ratio_t& r) {
        return l.a * r.b < r.a * l.b;
    }

    friend bool operator<=(const ratio_t& l, const ratio_t& r) {
        return !(l > r);
    }

    friend bool operator>(const ratio_t& l, const ratio_t& r) {
        return l.a * r.b > r.a * l.b;
    }

    friend bool operator>=(const ratio_t& l, const ratio_t& r) {
        return !(l < r);
    }

    friend bool operator==(const ratio_t& l, const ratio_t& r) {
        return l.a * r.b == r.a * l.b;
    }

    friend bool operator!=(const ratio_t& l, const ratio_t& r) {
        return !(l == r);
    }

    ratio_t inversed() const {
        return {b, a};
    }

    ratio_t minimized() const {
        auto g = gcd(a, b);

        return {a / g, b / g};
    }
};

template <class T>
std::ostream& operator<<(std::ostream& o, const ratio_t<T>& r) {
    return o << r.a << "/" << r.b;
}
