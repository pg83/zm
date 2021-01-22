#pragma once

#include "types.h"
#include "bigint.h"

#include <string>
#include <vector>

template <class R>
R from_string(const std::string& s);

template<>
inline bigint_t from_string<bigint_t>(const std::string& s) {
    return s;
}

template<>
inline int from_string<int>(const std::string& s) {
    return std::stoi(s);
}

template<>
inline unsigned int from_string<uint>(const std::string& s) {
    return (uint)std::stoul(s); //may overflow
}

template<>
inline long from_string<long>(const std::string& s) {
    return std::stol(s);
}

template<>
inline ulong from_string<ulong>(const std::string& s) {
    return std::stoul(s);
}

template<>
inline long long from_string<long long>(const std::string& s) {
    return std::stoll(s);
}

template<>
inline ulonglong from_string<ulonglong>(const std::string& s) {
    return std::stoull(s);
}
