#include <euler/lib/euler.h>

template <class T, class C>
C join(T t, C c) {
    C r;

    r.push_back(t);
    r.insert(r.end(), c.begin(), c.end());

    return r;
}

// https://msdn.microsoft.com/en-us/library/aa289166.aspx
template <class V>
void first_combination(int k, V& v) {
    for (int i = 0; i < k; ++i) {
        v.push_back(i);
    }
}

template <class V>
bool next_combination(int n, V& ans) {
    auto k = (int)ans.size();

    if (ans[0] == n - k) {
        return false;
    }

    auto i = k - 1;

    while (i > 0 && ans[i] == n - k + i) {
        i -= 1;
    }

    ans[i] += 1;

    for (int j = i; j < k - 1; ++j) {
        ans[j + 1] = ans[j] + 1;
    }

    return true;
}

struct combination_t: public std::vector<int> {
    int n;

    combination_t(int kk, int nn)
        : n(nn)
    {
        first_combination(kk, *this);
    }

    bool next() {
        return next_combination(n, *this);
    }
};

template <class V>
struct select_k_t {
    using values_t = std::vector<V>;

    combination_t comb;
    values_t values;

    select_k_t(int k, values_t v)
        : comb(k, v.size())
    {
        v.swap(values);
    }

    auto selected() const {
        values_t res;

        for (auto i : comb) {
            res.push_back(values[i]);
        }

        return res;
    }

    auto other() const {
        values_t res;
        std::set<int> sel(comb.begin(), comb.end());

        for (int i = 0; i < (int)values.size(); ++i) {
            if (sel.find(i) == sel.end()) {
                res.push_back(values[i]);
            }
        }

        return res;
    }

    bool next() {
        return comb.next();
    }
};

using ctx_t = std::vector<int>;
using res_t = ratio_t<int>;

struct term_i {
    virtual ~term_i() {
    }

    virtual res_t evaluate(const ctx_t& ctx) = 0;
    virtual std::string to_string() = 0;
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

    std::string to_string() override {
        return std::to_string(n + 1);
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

    std::string to_string() override {
        return "(" + lt->to_string() + " + " + rt->to_string() + ")";
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

    std::string to_string() override {
        return "(" + lt->to_string() + " - " + rt->to_string() + ")";
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

    std::string to_string() override {
        return "(" + lt->to_string() + " * " + rt->to_string() + ")";
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

    std::string to_string() override {
        return "(" + lt->to_string() + " / " + rt->to_string() + ")";
    }
};

static auto& all_terms() {
    static std::deque<std::unique_ptr<term_i>> terms;

    return terms;
}

template <class T, typename... Args>
T* new_term(Args&&... args) {
    auto res = new T(std::forward<Args>(args)...);

    all_terms().emplace_back(res);

    return res;
}

using terms_t = std::vector<term_i*>;

static terms_t generate_terms(int n) {
    terms_t res;

    auto calc = [&](auto& calc, const terms_t& t) -> void {
        if (t.size() == 1) {
            res.push_back(t.back());
        } else {
            select_k_t<term_i*> sel(2, t);

            do {
                auto s = sel.selected();
                auto o = sel.other();

                calc(calc, join(new_term<add_t>(s[0], s[1]), o));
                calc(calc, join(new_term<sub_t>(s[0], s[1]), o));
                calc(calc, join(new_term<sub_t>(s[1], s[0]), o));
                calc(calc, join(new_term<mul_t>(s[0], s[1]), o));
                calc(calc, join(new_term<diw_t>(s[0], s[1]), o));
                calc(calc, join(new_term<diw_t>(s[1], s[0]), o));
            } while (sel.next());
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

        for (auto term : terms) {
            try {
                auto x = term->evaluate(ctx);

                if (int n = 0; x.to_integer(n) && n > 0) {
                    if (res.find(n) == res.end()) {
                        res.insert(n);

                        //std::cout << x << ", " << n << " = " << term->to_string() << std::endl;
                    }
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
