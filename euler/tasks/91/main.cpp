#include <euler/lib/euler.h>

const auto N = 50;

int main() {
    auto a = 0;
    auto s = 0;

    auto is_ok = [](int x1, int y1, int x2, int y2) {
        auto a = x1 * x1 + y1 * y1;
        auto b = x2 * x2 + y2 * y2;
        auto c = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);

        return a > 0 && b > 0 && c > 0 && (a == b + c || b == a + c || c == a + b);
    };

    for (int x1 = 0; x1 <= N; ++x1) {
        for (int y1 = 0; y1 <= N; ++y1) {
            for (int x2 = 0; x2 <= N; ++x2) {
                for (int y2 = 0; y2 <= N; ++y2) {
                    if (is_ok(x1, y1, x2, y2)) {
                        if (x1 == y2 && x2 == y1) {
                            s += 1;
                        } else {
                            a += 1;
                        }
                    }
                }
            }
        }
    }

    std::cout << (a + s) / 2 << std::endl;
}
