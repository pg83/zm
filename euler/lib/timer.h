#pragma once

#include "types.h"

ui64 now_ms() noexcept;

struct prof_timer_t {
    const char* prefix;
    ui64 start;

    prof_timer_t(const char* p)
        : prefix(p)
        , start(now_ms())
    {
    }

    ~prof_timer_t() {
        out_diff(now_ms() - start);
    }

    void out_diff(ui64 ms) const;
};
