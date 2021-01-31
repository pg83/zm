#include "xxhash.h"

#include <tp/libs/xxhash/xxhash.h>

ui32 xx::hash32(const void* data, size_t len, ui32 seed) noexcept {
    return XXH32(data, len, seed);
}

ui64 xx::hash64(const void* data, size_t len, ui64 seed) noexcept {
    return XXH64(data, len, seed);
}
