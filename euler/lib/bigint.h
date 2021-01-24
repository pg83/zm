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

    // sub
    friend bigint_t operator-(const bigint_t& l, const bigint_t& r);

    bigint_t& operator-=(const bigint_t& v) {
        (*this - v).swap(*this);

        return *this;
    }

    bigint_t& operator--() {
        *this -= 1;

        return *this;
    }

    // mul
    friend bigint_t operator*(const bigint_t& l, const bigint_t& r);

    bigint_t& operator*=(const bigint_t& v) {
        (*this * v).swap(*this);

        return *this;
    }

    //div
    friend bigint_t operator%(const bigint_t& l, const bigint_t& r);

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

    //misc
    bigint_t reverse() const;
    std::string to_string() const;
    size_t digit_sum() const;
    size_t digit_count() const;

    void swap(bigint_t& v) noexcept {
        i_.swap(v.i_);
    }

private:
    struct impl_t;
    std::shared_ptr<impl_t> i_;
};

inline std::ostream& operator<<(std::ostream& os, const bigint_t& bi) {
    os << bi.to_string();

    return os;
}
