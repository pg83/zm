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

template <class T>
bool operator==(const fibo_iter_t<T>& l, const fibo_iter_t<T>& r) noexcept {
    return l.a_ == r.a_;
}

template <class T>
bool operator!=(const fibo_iter_t<T>& l, const fibo_iter_t<T>& r) noexcept {
    return !(l == r);
}

template <class T>
struct fibo_seq_t {
    fibo_iter_t<T> begin() const noexcept {
        return {T(1), T(1)};
    }

    fibo_iter_t<T> end() const noexcept {
        return {T(0), T(0)};
    }
};
