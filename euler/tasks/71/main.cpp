#include <euler/lib/euler.h>

int main() {
    auto max = ratio_t(3, 7);
    auto prev = ratio_t(0);

    for (auto it : farey_seq(1000000)) {
        if (it < max) {
            prev = it;
        } else {
            break;
        }
    }

    std::cout << prev.a << std::endl;
}
