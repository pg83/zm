#include <iostream>

static const unsigned data[] = {
    #include "data.h"
};

static unsigned xy(size_t x, size_t y) noexcept {
    return data[x + y * 20];
}

int main() {
    unsigned max = 0;

    for (size_t i = 0; i <= 16; ++i) {
        for (size_t j = 0; j <= 16; ++j) {
            const auto a1 = xy(i, j);
            const auto a2 = xy(i + 1, j);
            const auto a3 = xy(i + 2, j);
            const auto a4 = xy(i + 3, j);

            const auto b1 = xy(i, j);
            const auto b2 = xy(i, j + 1);
            const auto b3 = xy(i, j + 2);
            const auto b4 = xy(i, j + 3);

            const auto c1 = xy(i, j);
            const auto c2 = xy(i + 1, j + 1);
            const auto c3 = xy(i + 2, j + 2);
            const auto c4 = xy(i + 3, j + 3);

            const auto d1 = xy(i + 3, j);
            const auto d2 = xy(i + 2, j + 1);
            const auto d3 = xy(i + 1, j + 2);
            const auto d4 = xy(i, j + 3);

            const auto v1 = a1 * a2 * a3 * a4;
            const auto v2 = b1 * b2 * b3 * b4;
            const auto v3 = c1 * c2 * c3 * c4;
            const auto v4 = d1 * d2 * d3 * d4;

            if (v1 > max) {
                max = v1;
                std::cout << i << " " << j << " " << a1 << " " << a2 << " " << a3 << " " << a4  << std::endl;
            }

            if (v2 > max) {
                max = v2;
                std::cout << i << " " << j << " " << b1 << " " << b2 << " " << b3 << " " << b4  << std::endl;
            }

            if (v3 > max) {
                max = v3;
                std::cout << i << " " << j << " " << c1 << " " << c2 << " " << c3 << " " << c4  << std::endl;
            }

            if (v4 > max) {
                max = v4;
                std::cout << i << " " << j << " " << d1 << " " << d2 << " " << d3 << " " << d4  << std::endl;
            }
        }
    }

    std::cout << max << std::endl;
}
