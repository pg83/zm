#pragma once

#include <utility>
#include <optional>

template <class F>
struct result_of_f_t {
    using type_t = decltype(std::declval<F>()());
};

template <class F>
using result_of_t = typename result_of_f_t<F>::type_t;

struct stop_iteration_t {
};

struct any_iterator_end_t {
};

template <class F>
struct any_iterator_t {
    any_iterator_t(const F& f)
        : func(f)
    {
        next();
    }

    const auto& operator*() noexcept {
        return *cur;
    }

    any_iterator_t& operator++() {
        next();

        return *this;
    }

    friend bool operator==(const any_iterator_t& l, const any_iterator_end_t&) noexcept {
        return l.at_end();
    }

    friend bool operator!=(const any_iterator_t& l, const any_iterator_end_t&) noexcept {
        return !l.at_end();
    }

private:
    bool at_end() const noexcept {
        return !cur;
    }

    void next() {
        try {
            cur = func();
        } catch (const stop_iteration_t&) {
            cur.reset();
        }
    }

private:
    F func;
    std::optional<result_of_t<F>> cur;
};

template <class F>
struct any_sequence_t {
    F func;

    any_iterator_t<F> begin() const {
        return {func};
    }

    any_iterator_end_t end() const {
        return {};
    }
};

template <class F>
any_sequence_t<F> any_sequence(F&& f) {
    return {std::forward<F>(f)};
}
