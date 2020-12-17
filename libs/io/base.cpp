#include "base.h"

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
    char buf[1024];
    std::string ret;

    while (size_t res = read(buf, sizeof(buf))) {
        ret.append(buf, res);
    }

    return ret;
}
