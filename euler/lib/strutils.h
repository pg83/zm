#pragma once

#include "from_string.h"

#include <string>
#include <vector>

size_t digit_sum(const std::string& s) noexcept;

std::vector<std::string> split_string(const std::string& s, char delim);
std::vector<std::string> read_lines(const std::string& path);
std::vector<int> read_matrix(const std::string& path, char delim);

template <class R>
auto parse_string(const std::string& s, char delim) {
    std::vector<R> res;

    for (const auto& l : split_string(s, delim)) {
        res.push_back(from_string<R>(l));
    }

    return res;
}
