#include <euler/lib/euler.h>

static const std::string data[] = {
    #include "words.txt"
};

int main() {
    std::set<int> tn;

    for (int i = 0; i < 10000; ++i) {
        tn.insert((i * (i + 1)) / 2);
    }

    auto is_triangle = [&] (int n) -> bool {
        return tn.find(n) != tn.end();
    };

    auto alpha_weight = [](const std::string& s) -> int {
        int res = 0;

        for (auto ch : s) {
            res += ch - 'A' + 1;
        }

        return res;
    };

    size_t res = 0;

    for (size_t i = 0; i < std::size(data); ++i) {
        if (is_triangle(alpha_weight(data[i]))) {
            ++res;
        }
    }

    std::cout << res << std::endl;
}
