#include "base.h"
#include "str.h"

using namespace io;
using namespace std;

input_i::input_i() noexcept {
}

input_i::~input_i() {
}

size_t input_i::read_exact(void* d, size_t l) {
    auto b = (char*)d;

    while (l) {
        auto res = read(b, l);

        if (res == 0) {
            break;
        }

        l -= res;
        b += res;
    }

    return b - (char*)d;
}

std::string input_i::read_all() {
    std::string ret;
    str_output_t out(ret);

    read_all(out);

    return ret;
}

void input_i::read_all(output_i& out) {
    char buf[1024];

    while (size_t res = read(buf, sizeof(buf))) {
        out.write(buf, res);
    }
}

output_i::output_i() noexcept {
}

output_i::~output_i() {
}
