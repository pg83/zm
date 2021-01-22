#include <euler/lib/euler.h>

int main() {
    std::vector<int> e;

    e.push_back(2);

    for (int i = 1; i <= 100; ++i) {
        e.push_back(1);
        e.push_back(i * 2);
        e.push_back(1);
    }

    auto eval = eval_pq_t<int>([&](int n) -> int {
        return e[n];
    });

    std::cout << eval(99).first.digit_sum() << std::endl;
}
