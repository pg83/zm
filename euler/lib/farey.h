#pragma once

#include "ratio.h"

// farey sequence
template <class T>
struct farey_iterator_t {
    const T n;

    T a;
    T b;
    T c;
    T d;

    farey_iterator_t(T maxd)
        : n(maxd)
        , a(0)
        , b(1)
        , c(1)
        , d(n)
    {
    }

    ratio_t<T> operator*() const {
        return {a, b};
    }

    farey_iterator_t& operator++() {
        next();

        return *this;
    }

    void next() {
        auto k = (n + b) / d;

        auto a1 = c;
        auto b1 = d;
        auto c1 = k * c - a;
        auto d1 = k * d - b;

        a = a1;
        b = b1;
        c = c1;
        d = d1;
    }

    bool at_end() const {
        return a > b;
    }
};

struct farey_iterator_end_t {
};

template <class T>
bool operator==(const farey_iterator_t<T>& l, farey_iterator_end_t) {
    return l.at_end();
}

template <class T>
bool operator!=(const farey_iterator_t<T>& l, farey_iterator_end_t) {
    return !l.at_end();
}

template <class T>
struct farey_seq_t {
    T n;

    farey_seq_t(T n_)
        : n(n_)
    {
    }

    farey_iterator_t<T> begin() const {
        return {n};
    }

    farey_iterator_end_t end() const {
        return {};
    }
};

template <class T>
farey_seq_t<T> farey_seq(T n) {
    return {n};
}
