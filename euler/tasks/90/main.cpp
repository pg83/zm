#include <euler/lib/euler.h>

int main() {
    std::set<int> squares;

    for (int i = 1; i <= 9; ++i) {
        squares.insert(i * i);
    }

    auto is_ok = [&](const auto& m, const auto& n) -> bool {
        std::set<int> res;

        auto on_pair = [&](int i, int j) {
            res.insert(i * 10 + j);

            if (i == 6) {
                res.insert(9 * 10 + j);
            }

            if (i == 9) {
                res.insert(6 * 10 + j);
            }

            if (j == 6) {
                res.insert(i * 10 + 9);
            }

            if (j == 9) {
                res.insert(i * 10 + 6);
            }
        };

        for (auto i : m) {
            for (auto j : n) {
                on_pair(i, j);
                on_pair(j, i);
            }
        }

        for (auto sq : squares) {
            if (res.find(sq) == res.end()) {
                return false;
            }
        }

        return true;
    };

    auto res = 0;

    for (const auto& m : combination_sequence(6, 10)) {
        for (const auto& n : combination_sequence(6, 10)) {
            if (is_ok(m, n)) {
                res += 1;
            }
        }
    }

    std::cout << res / 2 << std::endl;;
}
