#include "mem.h"

#include <algorithm>

using namespace io;

memory_input_t::~memory_input_t() {
}

size_t memory_input_t::do_read(void* buf, size_t len) {
    auto to_read = std::min(left(), len);

    memcpy(buf, b_, to_read);
    b_ += to_read;

    return to_read;
}
