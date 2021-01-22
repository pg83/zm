#include <euler/lib/euler.h>

int main() {
    std::vector<int> v({0, 1, 2, 3, 4, 5, 6, 7, 8, 9});

    for (size_t i = 1; i < 1000000; ++i) {
        std::next_permutation(v.begin(), v.end());
    }

    std::string res;

    for (auto x : v) {
        res += std::to_string(x);
    }

    std::cout << res << std::endl;
}
