#include <euler/lib/euler.h>

int main() {
    for (int res = 1; ; ++res) {
        auto a = res;
        auto b = a + 1;
        auto c = a + 2;
        auto d = a + 3;

        if (uniq_prime_count(a) == 4) {
            if (uniq_prime_count(b) == 4) {
                if (uniq_prime_count(c) == 4) {
                    if (uniq_prime_count(d) == 4) {
                        std::cout << res << std::endl;

                        return 0;
                    }
                }
            }
        }
    }
}
