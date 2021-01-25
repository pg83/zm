#include <euler/lib/euler.h>

static double keyf(int m, int e) noexcept {
    return e * std::log(m);
}

int main() {
    size_t n = 0;
    size_t maxn = 0;
    double maxv = 0;

    for (const auto& line : read_lines("p099_base_exp.txt")) {
        auto be = parse_string<int>(line, ',');
        auto v = keyf(be[0], be[1]);

        if (v > maxv) {
            maxv = v;
            maxn = n;
        }

        ++n;
    }

    std::cout << maxn + 1 << std::endl;
}
