#pragma once

#include <libs/platform/types.h>

#include <string_view>

namespace xx {
    ui32 hash32(const void* data, size_t len, ui32 seed) noexcept;
    ui64 hash64(const void* data, size_t len, ui64 seed) noexcept;

    inline auto hash32(std::string_view data, ui32 seed) noexcept {
        return hash32(data.begin(), data.size(), seed);
    }

    inline auto hash64(std::string_view data, ui64 seed) noexcept {
        return hash64(data.begin(), data.size(), seed);
    }

    struct hash_t {
        template <class T>
        auto operator()(T&& t) const noexcept {
            if constexpr (sizeof(size_t) == 8) {
                return hash64(t.data(), t.size(), 0);
            } else {
                return hash32(t.data(), t.size(), 0);
            }
        }
    };
}
