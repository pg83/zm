#pragma once

#include <vector>

template <class T>
struct qir_t {
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

    qir_t inverse() const {
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

    friend qir_t operator*(T left, qir_t right) {
        return {right.a * left, right.x, right.b * left, right.c};
    }

    friend qir_t operator+(qir_t left, T right) {
        return {left.a, left.x, left.b + left.c * right, left.c};
    }

    friend qir_t operator-(qir_t left, T right) {
        return {left.a, left.x, left.b - left.c * right, left.c};
    }

    friend bool operator<(qir_t left, T right) {
        auto d = left.c * right - left.b;

        return left.a * left.a * left.x < d * d;
    }

    friend bool operator<(T left, qir_t right) {
        return !(right < left); // can not be equal
    }

    friend bool operator==(qir_t left, qir_t right) {
        return left.a == right.a && left.x == right.x && left.b == right.b && left.c == right.c;
    }

    friend bool operator!=(qir_t left, qir_t right) {
        return !(left == right);
    }

    static qir_t root_of(T n) {
        return {1, n, 0, 1};
    }

    std::vector<T> cont_fraction() const {
        std::vector<T> res;

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
};
