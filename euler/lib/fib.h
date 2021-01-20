#pragma once

template <class T>
struct fibo_iter_t {
    fibo_iter_t(T a, T b) noexcept
        : a_(a)
        , b_(b)
    {
    }

    void next() noexcept {
        auto x = a_;

        a_ = b_;
        b_ = b_ + x;
    }

    T operator*() noexcept {
        return a_;
    }

    fibo_iter_t& operator++() noexcept {
        next();

        return *this;
    }

    fibo_iter_t operator++(int) noexcept {
        auto it = *this;

        next();

        return it;
    }

    T a_ = 1;
    T b_ = 1;
};

struct fibo_iter_end_t {
};

template <class T>
bool operator==(const fibo_iter_t<T>&, const fibo_iter_end_t&) noexcept {
    return false;
}

template <class T>
bool operator!=(const fibo_iter_t<T>&, const fibo_iter_end_t&) noexcept {
    return true;
}

template <class T>
struct fibo_seq_t {
    fibo_iter_t<T> begin() const noexcept {
        return {T(1), T(1)};
    }

    fibo_iter_end_t end() const noexcept {
        return {};
    }
};
