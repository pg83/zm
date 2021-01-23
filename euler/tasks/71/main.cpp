#include <euler/lib/euler.h>

int main() {
    auto max = ratio_t(3, 7);
    auto prev = ratio_t(0);
    ui64 cnt = 0;

    for (auto it : farey_seq(1000000)) {
        ++cnt;

        if (cnt % 1000000000 == 0) {
            std::cout << cnt << std::endl;
        }

        if (it < max) {
            prev = it;
        } else {
            break;
        }
    }

    std::cout << prev.a << std::endl;
}
