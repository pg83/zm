#pragma once

#include <string_view>

#include <stdint.h>

namespace xxhash {
    uint32_t hash32(const void* data, size_t len, uint32_t seed) noexcept;
    uint64_t hash64(const void* data, size_t len, uint64_t seed) noexcept;

    inline uint32_t hash32(std::string_view data, uint32_t seed) noexcept {
        return hash32(data.begin(), data.size(), seed);
    }

    inline uint64_t hash64(std::string_view data, uint64_t seed) noexcept {
        return hash64(data.begin(), data.size(), seed);
    }
}
