#include "bigint.h"
#include "algo.h"
#include "strutils.h"

#include <tp/libs/tommath/tommath.h>

namespace {
    struct mp_error_t: public std::exception {
        mp_error_t(mp_err code)
            : c(code)
        {
        }

        const char* what() const noexcept override {
            return mp_error_to_string(c);
        }

        mp_err c;
    };

    static void check_err(mp_err code) {
        if (code != MP_OKAY) {
            throw mp_error_t(code);
        }
    }

    struct bignum_holder_t {
        bignum_holder_t() {
            check_err(mp_init(&bi));
        }

        ~bignum_holder_t() noexcept {
            mp_clear(&bi);
        }

        mp_int bi;
    };
}

struct bigint_t::impl_t: public bignum_holder_t {
    impl_t() {
    }

    impl_t(long num) {
        mp_set_l(&bi, num);
    }

    impl_t(const char* num) {
        check_err(mp_read_radix(&bi, num, 10));
    }

    std::string to_string() const {
        char buf[1024 * 16];
        size_t written = 0;

        check_err(mp_to_radix(&bi, buf, sizeof(buf), &written, 10));

        return std::string(buf, written - 1);
    }
};

bigint_t::bigint_t()
    : i_(new impl_t())
{
}

bigint_t::bigint_t(long num)
    : i_(new impl_t(num))
{
}

bigint_t::bigint_t(const char* num)
    : i_(new impl_t(num))
{
}

bigint_t::bigint_t(const std::string& num)
    : i_(new impl_t(num.c_str()))
{
}

bigint_t::~bigint_t() noexcept {
}

std::string bigint_t::to_string() const {
    return i_->to_string();
}

bigint_t operator+(const bigint_t& l, const bigint_t& r) {
    bigint_t res;

    check_err(mp_add(&l.i_->bi, &r.i_->bi, &res.i_->bi));

    return res;
}

bigint_t operator*(const bigint_t& l, const bigint_t& r) {
    bigint_t res;

    check_err(mp_mul(&l.i_->bi, &r.i_->bi, &res.i_->bi));

    return res;
}

bool operator<(const bigint_t& l, const bigint_t& r) {
    return mp_cmp(&l.i_->bi, &r.i_->bi) == MP_LT;
}

bool operator>(const bigint_t& l, const bigint_t& r) {
    return mp_cmp(&l.i_->bi, &r.i_->bi) == MP_GT;
}

bool operator==(const bigint_t& l, const bigint_t& r) {
    return mp_cmp(&l.i_->bi, &r.i_->bi) == MP_EQ;
}

bigint_t bigint_t::reverse() const {
    return reversed(to_string());
}

size_t bigint_t::digit_sum() const {
    return ::digit_sum(to_string());
}

size_t bigint_t::digit_count() const {
    return to_string().size();
}
