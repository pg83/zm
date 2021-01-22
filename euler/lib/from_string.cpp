#include "from_string.h"
#include "bigint.h"

template<>
bigint_t from_string<bigint_t>(const std::string& s) {
    return s;
}

template<>
int from_string<int>(const std::string& s) {
    return std::stoi(s);
}

template<>
uint from_string<uint>(const std::string& s) {
    return (uint)std::stoul(s); //may overflow
}

template<>
long from_string<long>(const std::string& s) {
    return std::stol(s);
}

template<>
ulong from_string<ulong>(const std::string& s) {
    return std::stoul(s);
}

template<>
long long from_string<long long>(const std::string& s) {
    return std::stoll(s);
}

template<>
ulonglong from_string<ulonglong>(const std::string& s) {
    return std::stoull(s);
}
