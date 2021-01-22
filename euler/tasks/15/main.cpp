#include <euler/lib/euler.h>

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
