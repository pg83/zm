#include "str.h"

using namespace io;

str_output_t::~str_output_t() {
}

void str_output_t::do_write(const void* data, size_t len) {
    s_.append((const char*)data, len);
}
