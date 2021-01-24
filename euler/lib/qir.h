#pragma once

#include <vector>

template <class T>
struct qir_t {
    using cont_fraction_t = std::vector<T>;

    T a;
    T x;
    T b;
    T c;

    qir_t reciprocal() const {
        return {c * a, x, -(b * c), a * a * x - b * b};
    }

    qir_t minimized() const {
        auto n = gcd(a, b, c);

        return {a / n, x, b / n, c / n};
    }

    auto inverse() const {
        return reciprocal().minimized();
    }

    T floor() const {
        T n = 0;
        T m = 1;

        while (m < *this) {
            m = m * 2;
        }

        while (m - n > 1) {
            auto k = n + (m - n) / 2;

            if (*this < k) {
                m = k;
            } else {
                n = k;
            }
        }

        return n;
    }

    friend qir_t operator*(T l, qir_t r) {
        return {r.a * l, r.x, r.b * l, r.c};
    }

    friend qir_t operator+(qir_t l, T r) {
        return {l.a, l.x, l.b + l.c * r, l.c};
    }

    friend qir_t operator-(qir_t l, T r) {
        return {l.a, l.x, l.b - l.c * r, l.c};
    }

    friend bool operator<(qir_t l, T r) {
        auto d = l.c * r - l.b;

        return l.a * l.a * l.x < d * d;
    }

    friend bool operator<(T l, qir_t r) {
        return !(r < l); // can not be equal
    }

    friend bool operator==(qir_t l, qir_t r) {
        return l.a == r.a && l.x == r.x && l.b == r.b && l.c == r.c;
    }

    friend bool operator!=(qir_t l, qir_t r) {
        return !(l == r);
    }

    static qir_t root_of(T n) {
        return {1, n, 0, 1};
    }

    auto cont_fraction() const {
        cont_fraction_t res;

        res.push_back(floor());

        auto n = (*this - res.back()).inverse();
        auto c = n;

        do {
            auto f = c.floor();

            res.push_back(f);

            c = (c - f).inverse();
        } while (c != n);

        return res;
    }

    auto cont_fraction_func() const {
        return [cf = cont_fraction()](size_t n) -> T {
            if (n == 0) {
                return cf[0];
            }

            return cf[1 + ((n - 1) % (cf.size() - 1))];
        };
    }
};
