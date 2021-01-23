#include <euler/lib/euler.h>

int main() {
    auto max = ratio_t(1, 2);
    auto min = ratio_t(1, 3);
    auto cnt = 0;

    for (auto it : farey_seq(12000)) {
        if (min < it && it < max) {
            ++cnt;
        }
    }

    std::cout << cnt << std::endl;
}
