#pragma once

#include <ostream>

template <class T, T N>
struct mod_int_t {
    T v;

    mod_int_t() noexcept
        : v(0)
    {
    }

    mod_int_t(T x) noexcept
        : v(x % N)
    {
    }

    friend mod_int_t operator*(mod_int_t l, mod_int_t r) noexcept {
        return l.v * r.v;
    }

    friend mod_int_t operator+(mod_int_t l, mod_int_t r) noexcept {
        return l.v + r.v;
    }

    mod_int_t& operator+=(mod_int_t x) noexcept {
        (*this + x).swap(*this);

        return *this;
    }

    void swap(mod_int_t& x) noexcept {
        std::swap(v, x.v);
    }
};

template <class T, T N>
std::ostream& operator<<(std::ostream& o, const mod_int_t<T, N>& v) {
    return o << "*" << v.v;
}
