#include <euler/lib/euler.h>

static bool do_check(bigint_t v, bigint_t vr, size_t c) {
    if (c > 50) {
        return true;
    }

    auto n = v + vr;
    auto r = n.reverse();

    if (n == r) {
        return false;
    }

    return do_check(n, r, c + 1);
}

static bool check(bigint_t v) {
    return do_check(v, v.reverse(), 0);
}

int main() {
    uint res = 0;

    for (uint i = 1; i < 10000; ++i) {
        if (check(i)) {
            ++res;
        }
    }

    std::cout << res << std::endl;
}
