#pragma once

#include <utility>

template <class F>
struct result_of_f_t {
    using type_t = decltype(std::declval<F>()());
};

template <class F>
using result_of_t = typename result_of_f_t<F>::type_t;

struct stop_iteration_t {
};

template <class F>
struct any_iterator_t {
    using res_t = result_of_t<F>;

    any_iterator_t(const F& f)
        : func(f)
        , at_end(false)
    {
        next();
    }

    void next() {
        if (!at_end) {
            try {
                cur = func();
            } catch (const stop_iteration_t&) {
                at_end = true;
            }
        }
    }

    const res_t& operator*() noexcept {
        return cur;
    }

    any_iterator_t& operator++() {
        next();

        return *this;
    }

    F func;
    res_t cur;
    bool at_end;
};

struct any_iterator_end_t {
};

template <class F>
bool operator==(const any_iterator_t<F>& l, const any_iterator_end_t&) noexcept {
    return l.at_end;
}

template <class F>
bool operator!=(const any_iterator_t<F>& l, const any_iterator_end_t&) noexcept {
    return !l.at_end;
}

template <class F>
struct any_sequence_t {
    F func;

    any_sequence_t(const F& f)
        : func(f)
    {
    }

    any_iterator_t<F> begin() const {
        return {func};
    }

    any_iterator_end_t end() const {
        return {};
    }
};

template <class F>
auto any_sequence(F&& f) {
    return any_sequence_t(std::forward<F>(f));
}
