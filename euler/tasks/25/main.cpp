#include <euler/lib/euler.h>

int main() {
    size_t cnt = 0;

    for (auto x : fibo_sequence<bigint_t>()) {
        ++cnt;

        if (x.digit_count() >= 1000) {
            break;
        }
    }

    std::cout << cnt << std::endl;
}
