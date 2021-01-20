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

uint64_t input_i::read_all(output_i& out) {
    return transfer_data(*this, out);
}

bool input_i::read_line(std::string& l) {
    const auto res = read_to(l, '\n');

    if (res && !l.empty() && l.back() == '\r') {
        l.pop_back();
    }

    return res;
}

size_t input_i::read_to(std::string& l, char to) {
    char ch;

    if (!read_char(ch)) {
        return 0;
    }

    l.clear();

    size_t result = 0;

    do {
        ++result;

        if (ch == to) {
            break;
        }

        l += ch;
    } while (read_char(ch));

    return result;
}

uint64_t io::transfer_data(input_i& in, output_i& out) {
    char buf[1024];
    uint64_t ret = 0;

    while (size_t res = in.read(buf, sizeof(buf))) {
        out.write(buf, res);
        ret += res;
    }

    return ret;
}

output_i::output_i() noexcept {
}

output_i::~output_i() {
}
