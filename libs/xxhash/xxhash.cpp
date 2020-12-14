#include "xxhash.h"

#include <tp/libs/xxhash/xxhash.h>

uint32_t xxhash::hash32(const void* data, size_t len, uint32_t seed) noexcept {
    return XXH32(data, len, seed);
}

uint64_t xxhash::hash64(const void* data, size_t len, uint64_t seed) noexcept {
    return XXH64(data, len, seed);
}
