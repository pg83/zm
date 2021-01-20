#pragma once

#include "base.h"

namespace io {
    class memory_input_t: public input_i {
    public:
        memory_input_t(const void* buf, size_t len) noexcept
            : b_((const char*)buf)
            , e_(b_ + len)
        {
        }

        ~memory_input_t() override;

        size_t left() const noexcept {
            return e_ - b_;
        }

    private:
        size_t do_read(void* buf, size_t len) override;

    private:
        const char* b_;
        const char* e_;
    };
}
