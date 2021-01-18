#pragma once

#include <string>
#include <ostream>

class bigint_t {
public:
    bigint_t();
    bigint_t(const char* num);
    bigint_t(const std::string& num);
    ~bigint_t() noexcept;

    std::string to_string() const;

    void swap(bigint_t& v) noexcept {
        i_.swap(v.i_);
    }

    friend bigint_t operator+(const bigint_t& l, const bigint_t& r);

    bigint_t& operator+=(const bigint_t& v) {
        (*this + v).swap(*this);

        return *this;
    }

private:
    struct impl_t;
    std::shared_ptr<impl_t> i_;
};

inline std::ostream& operator<<(std::ostream& os, const bigint_t& bi) {
    os << bi.to_string();

    return os;
}
