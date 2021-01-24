#include <euler/lib/euler.h>

template <class T, class F>
void primitive_triangles(T p, F&& cb) {
    auto s = sqrt_int(p);

    for (T m = 1; m <= s; ++m) {
        for (T n = 1, maxn = p / (2 * m); n <= maxn; ++n) {
            if (m > n && co_prime(m, n) && (m % 2 + n % 2) < 2) {
                auto a = m * m - n * n;
                auto b = 2 * m * n;
                auto c = m * m + n * n;

                if (a + b + c <= p) {
                    if (a < b) {
                        cb(a, b, c);
                    } else {
                        cb(b, c, a);
                    }
                }
            }
        }
    }
}

template <class T, class F>
void for_all_triangles(T p, F&& f) {
    primitive_triangles(p, [&] (T a, T b, T c) {
        auto s = a + b + c;
        auto k = 1;

        while (s * k <= p) {
            f(k * a, k * b, k * c);
            k += 1;
        }
    });
}

int main() {
    std::map<int, int> r;

    for_all_triangles<ui64>(1500000, [&](int a, int b, int c) {
        ++r[a + b + c];
    });

    auto s = 0;

    for (const auto& it : r) {
        if (it.second == 1) {
            ++s;
        }
    }

    std::cout << s << std::endl;
}
