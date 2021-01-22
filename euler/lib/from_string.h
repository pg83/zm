#pragma once

#include "types.h"

#include <string>

class bigint_t;

template <class R>
R from_string(const std::string& s);

template<>
bigint_t from_string<bigint_t>(const std::string& s);

template<>
int from_string<int>(const std::string& s);

template<>
uint from_string<uint>(const std::string& s);

template<>
long from_string<long>(const std::string& s);

template<>
ulong from_string<ulong>(const std::string& s);

template<>
long long from_string<long long>(const std::string& s);

template<>
ulonglong from_string<ulonglong>(const std::string& s);
