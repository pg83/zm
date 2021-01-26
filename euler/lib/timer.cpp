#include "timer.h"
#include "euler.h"

#include <sys/time.h>

ui64 now_ms() noexcept {
    struct timeval tv;

    memset(&tv, 0, sizeof(tv));
    gettimeofday(&tv, 0);

    return (ui64)tv.tv_sec * (ui64)1000000 + tv.tv_usec;
}

void timer_t::out_diff(ui64 ms) const {
    std::cout << prefix << ": " << (ms / 1000000.0) << " seconds elapsed" << std::endl;
}
