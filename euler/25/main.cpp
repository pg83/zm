#include <euler/lib/bigint.h>
#include <euler/lib/fib.h>

#include <iostream>

int main() {
    size_t cnt = 0;

    for (auto x : fibo_seq_t<bigint_t>()) {
        ++cnt;

        if (x.to_string().length() >= 1000) {
            break;
        }
    }

    std::cout << cnt << std::endl;
}
