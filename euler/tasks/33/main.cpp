#include <euler/lib/euler.h>

int main() {
    auto xn = 1;
    auto xm = 1;

    std::set<int> res;

    auto check = [&] (int n1, int n2, int m1, int m2, int n, int m) {
        if (n1 == 0) {
            return;
        }

        if (m1 == 0) {
            return;
        }

        if (n2 == 0 && m2 == 0) {
            return;
        }

        auto nn = 10 * n1 + n2;
        auto mm = 10 * m1 + m2;

        if (nn >= mm) {
            return;
        }

        if (nn * m == mm * n) {
            auto key = nn * 100 + mm;

            if (res.find(key) != res.end()) {
            } else {
                res.insert(key);

                xn *= nn;
                xm *= mm;

                std::cout << nn << " " << mm << std::endl;
            }
        }
    };

    for (int a = 0; a <= 9; ++a) {
        for (int b = 0; b <= 9; ++b) {
            for (int c = 0; c <= 9; ++c) {
                if (a == b) {
                } else if (b == c) {
                } else if (a == c) {
                } else {
                    check(a, b, b, c, a, c);
                    check(a, b, c, b, a, c);
                    check(b, a, b, c, a, c);
                    check(b, a, c, b, a, c);
                }
            }
        }
    }

    std::cout << xm / gcd(xn, xm) << std::endl;
}
