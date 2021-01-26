#include <euler/lib/euler.h>

static inline auto gen_big_num() {
    timer_t timer(__PRETTY_FUNCTION__);

    return pow_int(bigint_t(2), 10000000);
}

int main() {
    auto num = gen_big_num();

    {
        timer_t timer("check");

        for (int i = 0; i < 1000; ++i) {
            auto bn = pow_int(bigint_t(i), i);

            if (bn.to_string() != bn.to_string_tom()) {
                abort();
            }
        }
    }

    {
        timer_t timer("bigint_t::to_string()");

        std::cout << num.to_string().size() << std::endl;
    }

    {
        timer_t timer("bigint_t::to_string_tom()");

        std::cout << num.to_string_tom().size() << std::endl;
    }
}
