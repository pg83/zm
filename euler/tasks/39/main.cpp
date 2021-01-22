#include <euler/lib/euler.h>

int count_triangles(int p) {
    int res = 0;

    for (int a = 1; a < p; ++a) {
        for (int b = 1; b < p; ++b) {
            auto c = p - a - b;

            if (c > 0) {
                if (a * a + b * b == c * c) {
                    ++res;
                }
            } else {
                break;
            }
        }
    }

    return res;
}

int main() {
    int maxt = 0;
    int maxp = 0;

    for (int p = 1; p <= 1000; ++p) {
        auto t = count_triangles(p);

        if (t > maxt) {
            maxt = t;
            maxp = p;

            std::cout << maxp << " " << maxt << std::endl;
        }
    }

    std::cout << maxp << std::endl;
}
