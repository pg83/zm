#include <euler/lib/euler.h>

template <class T, class C>
std::string multiply(T n, const C& c) {
    std::string res;

    for (auto i : c) {
        res += std::to_string(n * i);
    }

    return res;
}

static bool is_pandigital(std::string s) noexcept {
    std::sort(s.begin(), s.end());

    return s == "123456789";
}

int main() {
    std::vector<int> tmp;
    std::vector<std::string> res;

    tmp.push_back(1);

    for (int m = 2; m <= 9; ++m) {
        tmp.push_back(m);

        for (int j = 0; j < 100000; ++j) {
            auto mult = multiply(j, tmp);

            if (is_pandigital(mult)) {
                res.push_back(mult);
            }
        }
    }

    std::sort(res.begin(), res.end());

    std::cout << res.back() << std::endl;
}
