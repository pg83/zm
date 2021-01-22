#include <euler/lib/euler.h>

static const char* data[] = {
    #include "data.h"
};

int main() {
    bigint_t res;

    for (size_t i = 0; i < sizeof(data) / sizeof(*data); ++i) {
        res += data[i];
    }

    std::cout << res << std::endl;
}
