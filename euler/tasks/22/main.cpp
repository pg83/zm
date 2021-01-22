#include <euler/lib/euler.h>

static std::string names[] = {
    #include "names.h"
};

static int weight(const std::string& w) {
    int res = 0;

    for (auto ch : w) {
        res += 1 + ch - 'A';
    }

    return res;
}

int main() {
    size_t cnt = sizeof(names) / sizeof(*names);
    std::sort(names, names + cnt);
    int res = 0;

    for (size_t i = 0; i < cnt; ++i) {
        int w = (i + 1) * weight(names[i]);

        std::cout << names[i] << " " << w << std::endl;

        res += w;
    }

    std::cout << res << std::endl;
}
