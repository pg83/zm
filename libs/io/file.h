#pragma once

#include "base.h"

#include <string>
#include <utility>

namespace io {
    class file_input_t: public input_i {
    public:
        file_input_t(const char* path);
        file_input_t(const std::string& path);

        ~file_input_t() override;

    private:
        size_t do_read(void* data, size_t len) override;

    private:
        struct impl_t;
        std::unique_ptr<impl_t> impl_;
    };
}
