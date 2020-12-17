#include "file.h"

#include <system_error>

#include <stdio.h>

using namespace io;

struct file_input_t::impl_t {
    impl_t(const char* path)
        : f_(fopen(path, "rb"))
    {
        if (!f_) {
            throw std::system_error(errno, std::system_category(), "can not open file " + std::string(path));
        }
    }

    ~impl_t() noexcept {
        fclose(f_);
    }

    size_t read(void* d, size_t l) {
        auto res = (size_t)fread(d, 1, l, f_);

        if (res < l) {
            if (ferror(f_) != 0) {
                throw std::system_error(errno, std::system_category(), "can not read file");
            }
        }

        return res;
    }

    FILE* f_;
};

file_input_t::file_input_t(const char* path)
    : impl_(new impl_t(path))
{
}

file_input_t::file_input_t(const std::string& path)
    : file_input_t(path.c_str())
{
}

file_input_t::~file_input_t() {
}

size_t file_input_t::do_read(void* data, size_t len) {
    return impl_->read(data, len);
}
