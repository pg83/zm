#include "bigint.h"
#include "euler.h"

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

    std::string to_string_tom() const {
        try {
            char buf[1024 * 16];
            size_t written = 0;

            check_err(mp_to_radix(&bi, buf, sizeof(buf), &written, 10));

            return std::string(buf, written - 1);
        } catch (...) {
            return to_string_tom_slow();
        }
    }

    std::string to_string_tom_slow() const {
        size_t nbuf = digit_count() + 16;
        char* buf = (char*)malloc(nbuf);

        Z_DEFER {
            free(buf);
        };

        size_t written = 0;

        check_err(mp_to_radix(&bi, buf, nbuf, &written, 10));

        return std::string(buf, written - 1);
    }

    size_t digit_count() const {
        size_t res = 0;

        check_err(mp_radix_size(&bi, 10, &res));

        return res - 1;
    }

    bool is_negative() const noexcept {
        return mp_isneg(&bi);
    }
};

bigint_t::impl_ref_t bigint_t::construct(long v) {
    struct small_t: public std::vector<impl_ref_t> {
        small_t() {
            for (long i = 0; i < 1000; ++i) {
                push_back(impl_ref_t(new impl_t(i)));
            }
        }
    };

    static const small_t small;

    if (v >= 0 && v < (long)small.size()) {
        return small[v];
    }

    return impl_ref_t(new impl_t(v));
}

bigint_t::impl_ref_t bigint_t::construct() {
    return impl_ref_t(new impl_t());
}

bigint_t::bigint_t()
    : i_(construct(0))
{
}

bigint_t::bigint_t(long num)
    : i_(construct(num))
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

bigint_t::bigint_t(impl_ref_t ref) noexcept
    : i_(ref)
{
}

bigint_t::~bigint_t() noexcept {
}

static std::string to_string_fast(bigint_t n) {
    static const bigint_t max = pow_int(bigint_t(10), 200);

    if (n < max) {
        return n.to_string_tom();
    }

    auto hdc = n.digit_count() / 2;
    auto big = pow_int(bigint_t(10), hdc);

    auto a = to_string_fast(n / big);
    auto b = to_string_fast(n % big);
    auto c = std::string(hdc - b.size(), '0');

    return a + c + b;
}

std::string bigint_t::to_string() const {
    if (is_negative()) {
        return "-" + to_string_fast(abs());
    }

    return to_string_fast(*this);
}

std::string bigint_t::to_string_tom() const {
    return i_->to_string_tom();
}

bigint_t operator+(const bigint_t& l, const bigint_t& r) {
    auto res = bigint_t::construct();

    check_err(mp_add(&l.i_->bi, &r.i_->bi, &res->bi));

    return res;
}

bigint_t operator-(const bigint_t& l, const bigint_t& r) {
    auto res = bigint_t::construct();

    check_err(mp_sub(&l.i_->bi, &r.i_->bi, &res->bi));

    return res;
}

bigint_t operator*(const bigint_t& l, const bigint_t& r) {
    auto res = bigint_t::construct();

    check_err(mp_mul(&l.i_->bi, &r.i_->bi, &res->bi));

    return res;
}

bigint_t operator%(const bigint_t& l, const bigint_t& r) {
    auto res = bigint_t::construct();

    check_err(mp_mod(&l.i_->bi, &r.i_->bi, &res->bi));

    return res;
}

bigint_t operator/(const bigint_t& l, const bigint_t& r) {
    auto res = bigint_t::construct();

    check_err(mp_div(&l.i_->bi, &r.i_->bi, &res->bi, 0));

    return res;
}

bigint_t bigint_t::abs() const {
    auto res = bigint_t::construct();

    check_err(mp_abs(&i_->bi, &res->bi));

    return res;
}

bigint_t bigint_t::sqrt() const {
    auto res = bigint_t::construct();

    check_err(mp_sqrt(&i_->bi, &res->bi));

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
    return i_->digit_count();
}

bool bigint_t::is_negative() const noexcept {
    return i_->is_negative();
}

bool bigint_t::is_even() const noexcept {
    return mp_iseven(&i_->bi);
}

bool bigint_t::is_odd() const noexcept {
    return mp_isodd(&i_->bi);
}
