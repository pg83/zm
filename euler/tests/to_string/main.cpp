#include <euler/lib/euler.h>

static inline auto gen_big_num() {
    timer_t timer(__PRETTY_FUNCTION__);

    return pow_int(bigint_t(2), 100000);
}

int main() {
    auto num = gen_big_num();

    {
        timer_t timer("bigint_t::to_string()");

        std::cout << num.to_string().size() << std::endl;
    }
}
