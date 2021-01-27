#include <euler/lib/euler.h>

int main() {
    std::vector<ui64> res;
    std::vector<int> d;

    d.push_back(1);

    for (int i = 2; i <= 9; ++i) {
        d.push_back(i);

        for (auto tmp : permutation_sequence(d)) {
            auto n = to_number<ui64>(tmp);

            if (is_prime_stupid(n)) {
                res.push_back(n);
            }
        }
    }

    std::sort(res.begin(), res.end());

    std::cout << res.back() << std::endl;
}
