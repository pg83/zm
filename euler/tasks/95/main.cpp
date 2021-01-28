#include <euler/lib/euler.h>

int main() {
    std::map<long, long> next;

    std::cout << proper_divisors_sum(28) << std::endl;

    for (long i = 2; i <= 1000000; ++i) {
        next[i] = proper_divisors_sum(i);
    }

    next[1] = 1;

    auto chain = [&](long n) -> std::optional<std::set<long>> {
        std::set<long> r;
        auto c = n;

        while (true) {
            r.insert(c);

            c = next.find(c)->second;

            if (c > 1000000) {
                return {};
            }

            if (c == n) {
                return r;
            }

            // cycle?
            if (r.find(c) != r.end()) {
                return {};
            }
        }
    };

    std::set<long> r;

    for (long i = 2; i < 1000000; ++i) {
        if (auto ch = chain(i); ch) {
            if (ch->size() > r.size()) {
                r = *ch;
            }
        }
    }

    std::cout << *r.begin() << std::endl;
}
