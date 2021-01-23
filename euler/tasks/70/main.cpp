#include <euler/lib/euler.h>

static int perm_hash(int n) noexcept {
    int res = 0;

    while (n > 0) {
        res += n % 10;
        n /= 10;
    }

    return res;
}

static std::string strong_hash(int v) {
    return sorted(std::to_string(v));
}

static bool is_perm(int l, int r) {
    return perm_hash(l) == perm_hash(r) && strong_hash(l) == strong_hash(r);
}

int main() {
    auto minrat = 200.0;
    auto minn = 0;

    for (int n = 2; n <= 10000000; ++n) {
        auto phi = euler_totient(n);
        auto rat = double(n) / double(phi);

        if (rat < minrat) {
            if (is_perm(phi, n)) {
                std::cout << n << " " << phi << " " << rat << std::endl;

                minrat = rat;
                minn = n;
            }
        }
    }

    std::cout << minn << std::endl;
}
