#include <euler/lib/euler.h>

int main() {
    auto pd = std::numeric_limits<int>::max();
    auto ar = 0;

    for (int n = 1; n <= 2000; ++n) {
        for (int m = 1; m <= 2000; ++m) {
            auto s = ((n * (n + 1)) / 2) * ((m * (m + 1)) / 2);

            if (s > 3000000) {
                break;
            }

            auto d = s - 2000000;
            auto dd = d > 0 ? d : -d;

            if (dd < pd) {
                pd = dd;
                ar = n * m;
            }
        }
    }

    std::cout << ar << std::endl;
}
