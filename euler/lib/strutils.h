#pragma once

#include "from_string.h"

#include <string>
#include <vector>

size_t dig_sum(const std::string& s) noexcept;

std::vector<std::string> split_string(const std::string& s, char delim);
std::vector<std::string> read_lines(const std::string& path);

template <class R>
std::vector<R> parse_string(const std::string& s, char delim) {
    std::vector<R> res;

    for (const auto& l : split_string(s, delim)) {
        res.push_back(from_string<R>(l));
    }

    return res;
}
