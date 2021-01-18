#include <map>
#include <functional>
#include <iostream>

template <class X, class R>
struct cacher1_t {
    template <class F>
    cacher1_t(F&& ff) {
        f = [ff, this] (X x) -> R {
            auto& cc = c;

            if (cc.find(x) == cc.end()) {
                cc[x] = ff(x, *this);
            }

            return cc[x];
        };
    }

    R operator()(X x) {
        return f(x);
    }

    std::map<X, R> c;
    std::function<R (X)> f;
};

template <class X, class Y, class R>
struct cacher2_t {
    template <class F>
    cacher2_t(F&& ff) {
        f = [ff, this] (X x, Y y) -> R {
            auto& cc = c[y];

            if (cc.find(x) == cc.end()) {
                cc[x] = ff(x, y, *this);
            }

            return cc[x];
        };
    }

    R operator()(X x, Y y) {
        return f(x, y);
    }

    std::map<Y, std::map<X, R>> c;
    std::function<R (X, Y)> f;
};

int main() {
    auto f = cacher2_t<int, int, unsigned long>([] (int n, int m, auto& f) -> unsigned long {
        if (n == 0) {
            return 1;
        }

        if (m == 0) {
            return 1;
        }

        return f(n - 1, m) + f(n, m - 1);
    });

    std::cout << f(20, 20) << std::endl;
}
