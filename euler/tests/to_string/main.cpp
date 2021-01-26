#include <euler/lib/euler.h>

static inline auto gen_big_num() {
    timer_t timer(__PRETTY_FUNCTION__);

    return pow_int(bigint_t(2), 1000000);
}

static std::string to_string_1(bigint_t n) {
    return n.to_string();
}

static std::string to_string_0(bigint_t n) {
    return n.to_string_tom();
}

int main() {
    auto num = gen_big_num();

    {
        timer_t timer("check");

        for (int i = 0; i < 1000; ++i) {
            auto bn = pow_int(bigint_t(i), i);

            if (to_string_0(bn) != to_string_1(bn)) {
                abort();
            }
        }
    }

    {
        timer_t timer("to_string_1()");

        std::cout << to_string_1(num).size() << std::endl;
    }

    {
        timer_t timer("to_string_0()");

        std::cout << to_string_0(num).size() << std::endl;
    }
}
