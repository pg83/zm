#pragma once

#include <libs/platform/types.h>

#include <string_view>

namespace resource {
    void store(const void* key_data, int key_size, const void* value_data, int value_size);
    void store(std::string_view path, std::string_view data);

    std::string_view load(std::string_view path);
    std::string_view key(size_t n) noexcept;
    std::string_view index(size_t n) noexcept;
    size_t count() noexcept;
}
