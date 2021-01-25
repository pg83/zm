#pragma once

#include <cstdint>
#include <cstddef>
#include <ostream>

using uchar = unsigned char;
using ushort = unsigned short;
using uint = unsigned int;
using ulong = unsigned long;
using ulonglong = unsigned long long;

using ui8 = uint8_t;
using ui16 = uint16_t;
using ui32 = uint32_t;
using ui64 = uint64_t;
using ui128 = __uint128_t;

using i8 = int8_t;
using i16 = int16_t;
using i32 = int32_t;
using i64 = int64_t;
using i128 = __int128_t;

void out(std::ostream& o, ui128 v);
void out(std::ostream& o, i128 v);

inline std::ostream& operator<<(std::ostream& o, ui128 v) {
    out(o, v);

    return o;
}

inline std::ostream& operator<<(std::ostream& o, i128 v) {
    out(o, v);

    return o;
}
