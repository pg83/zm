#pragma once

#include <string>
#include <vector>

std::vector<std::string> split_string(const std::string& s, char delim);
std::vector<std::string> read_lines(const std::string& path);

template <class R>
R from_string(const std::string& s);

template<>
inline int from_string<int>(const std::string& s) {
    return std::stoi(s);
}

template<>
inline unsigned int from_string<unsigned int>(const std::string& s) {
    return (unsigned int)std::stoul(s); //may overflow
}

template<>
inline long from_string<long>(const std::string& s) {
    return std::stol(s);
}

template<>
inline unsigned long from_string<unsigned long>(const std::string& s) {
    return std::stoul(s);
}

template<>
inline long long from_string<long long>(const std::string& s) {
    return std::stoll(s);
}

template<>
inline unsigned long long from_string<unsigned long long>(const std::string& s) {
    return std::stoull(s);
}

template <class R>
std::vector<R> parse_string(const std::string& s, char delim) {
    std::vector<R> res;

    for (const auto& l : split_string(s, delim)) {
        res.push_back(from_string<R>(l));
    }

    return res;
}
