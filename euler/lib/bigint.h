#pragma once

#include <string>
#include <ostream>

class bigint_t {
public:
    bigint_t();
    bigint_t(long num);
    bigint_t(const char* num);
    bigint_t(const std::string& num);
    ~bigint_t() noexcept;

    std::string to_string() const;

    void swap(bigint_t& v) noexcept {
        i_.swap(v.i_);
    }

    // sum
    friend bigint_t operator+(const bigint_t& l, const bigint_t& r);

    bigint_t& operator+=(const bigint_t& v) {
        (*this + v).swap(*this);

        return *this;
    }

    bigint_t& operator++() {
        *this += 1;

        return *this;
    }

    // mul
    friend bigint_t operator*(const bigint_t& l, const bigint_t& r);

    bigint_t& operator*=(const bigint_t& v) {
        (*this * v).swap(*this);

        return *this;
    }

    // cmp
    friend bool operator<(const bigint_t& l, const bigint_t& r);

    friend bool operator<=(const bigint_t& l, const bigint_t& r) {
        return !(l > r);
    }

    friend bool operator>(const bigint_t& l, const bigint_t& r);

    friend bool operator>=(const bigint_t& l, const bigint_t& r) {
        return !(l < r);
    }

    friend bool operator==(const bigint_t& l, const bigint_t& r);

    friend bool operator!=(const bigint_t& l, const bigint_t& r) {
        return !(l == r);
    }

private:
    struct impl_t;
    std::shared_ptr<impl_t> i_;
};

inline std::ostream& operator<<(std::ostream& os, const bigint_t& bi) {
    os << bi.to_string();

    return os;
}
