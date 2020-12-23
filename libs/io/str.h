#pragma once

#include "base.h"

#include <string>

namespace io {
    class str_output_t: public output_i {
    public:
        str_output_t(std::string& s) noexcept
            : s_(s)
        {
        }

        ~str_output_t() override;

    private:
        void do_write(const void* data, size_t len) override;

    private:
        std::string& s_;
    };
}
