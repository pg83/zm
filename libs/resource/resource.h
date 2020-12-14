#pragma once

#include <string_view>

namespace resource {
    void store(std::string_view path, std::string_view data);
    std::string_view load(std::string_view path);
    std::string_view index(size_t n) noexcept;
    size_t count() noexcept;

    struct reg_helper_t {
        inline reg_helper_t(std::string_view path, std::string_view data) {
            store(path, data);
        }
    };
}
