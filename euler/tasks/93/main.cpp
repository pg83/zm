#include <euler/lib/euler.h>

template <class V>
auto select_k_sequence(int k, const V& values) {
    return transform_sequence(combination_sequence(k, values.size()), [&values](const auto& b) mutable {
        std::set<int> sel(b.begin(), b.end());

        V other;
        V select;

        for (int i = 0; i < (int)values.size(); ++i) {
            if (sel.find(i) == sel.end()) {
                other.push_back(values[i]);
            } else {
                select.push_back(values[i]);
            }
        }

        return std::make_pair(select, other);
    });
}

using ctx_t = std::vector<int>;
using res_t = ratio_t<int>;

struct term_i {
    virtual ~term_i() {
    }

    virtual res_t evaluate(const ctx_t& ctx) = 0;
};

struct val_t: public term_i {
    int n;

    val_t(int nn) noexcept
        : n(nn)
    {
    }

    res_t evaluate(const ctx_t& ctx) override {
        return ctx[n];
    }
};

struct add_t: public term_i {
    term_i* lt;
    term_i* rt;

    add_t(term_i* l, term_i* r) noexcept
        : lt(l)
        , rt(r)
    {
    }

    res_t evaluate(const ctx_t& ctx) override {
        return lt->evaluate(ctx) + rt->evaluate(ctx);
    }
};

struct sub_t: public term_i {
    term_i* lt;
    term_i* rt;

    sub_t(term_i* l, term_i* r) noexcept
        : lt(l)
        , rt(r)
    {
    }

    res_t evaluate(const ctx_t& ctx) override {
        return lt->evaluate(ctx) - rt->evaluate(ctx);
    }
};

struct mul_t: public term_i {
    term_i* lt;
    term_i* rt;

    mul_t(term_i* l, term_i* r) noexcept
        : lt(l)
        , rt(r)
    {
    }

    res_t evaluate(const ctx_t& ctx) override {
        return lt->evaluate(ctx) * rt->evaluate(ctx);
    }
};

struct zero_div_t {
};

template <class T>
static T check_zero(const T& t) {
    if (t == 0) {
        throw zero_div_t();
    }

    return t;
}

struct diw_t: public term_i {
    term_i* lt;
    term_i* rt;

    diw_t(term_i* l, term_i* r) noexcept
        : lt(l)
        , rt(r)
    {
    }

    res_t evaluate(const ctx_t& ctx) override {
        return lt->evaluate(ctx) / check_zero(rt->evaluate(ctx));
    }
};

static auto& all_terms() {
    static std::deque<std::unique_ptr<term_i>> terms;

    return terms;
}

template <class T, typename... Args>
T* new_term(Args&&... args) {
    auto res = std::make_unique<T>(std::forward<Args>(args)...);

    all_terms().emplace_back(res.get());

    return res.release();
}

using terms_t = std::vector<term_i*>;

static terms_t generate_terms(int n) {
    terms_t res;

    auto calc = [&](auto& calc, const terms_t& t) -> void {
        if (t.size() == 1) {
            res.push_back(t.back());
        } else {
            for (auto [s, o]: select_k_sequence(2, t)) {
                calc(calc, prepend_el(new_term<add_t>(s[0], s[1]), o));
                calc(calc, prepend_el(new_term<sub_t>(s[0], s[1]), o));
                calc(calc, prepend_el(new_term<sub_t>(s[1], s[0]), o));
                calc(calc, prepend_el(new_term<mul_t>(s[0], s[1]), o));
                calc(calc, prepend_el(new_term<diw_t>(s[0], s[1]), o));
                calc(calc, prepend_el(new_term<diw_t>(s[1], s[0]), o));
            }
        }
    };

    {
        terms_t vals;

        for (int i = 0; i < n; ++i) {
            vals.push_back(new_term<val_t>(i));
        }

        calc(calc, vals);
    }

    return res;
}

int main() {
    auto terms = generate_terms(4);

    auto apply = [&](const ctx_t& ctx) -> int {
        std::set<int> res;

        for (const auto& term : terms) {
            try {
                auto x = term->evaluate(ctx);

                if (int n = 0; x.to_integer(n) && n > 0) {
                    res.insert(n);
                }
            } catch (const zero_div_t&) {
            }
        }

        int s = 1;

        for (auto v : res) {
            if (v != s) {
                break;
            }

            ++s;
        }

        return s - 1;
    };

    int maxv = 0;

    for (int a = 1; a <= 9; ++a) {
        for (int b = 1; b <= 9; ++b) {
            for (int c = 1; c <= 9; ++c) {
                for (int d = 1; d <= 9; ++d) {
                    if (a < b && b < c && c < d) {
                        auto res = apply({a, b, c, d});

                        if (res > maxv) {
                            maxv = res;

                            std::cout << a << b << c << d << std::endl;
                        }
                    }
                }
            }
        }
    }
}
