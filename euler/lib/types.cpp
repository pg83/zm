#include "types.h"
#include "algo.h"

#include <string>

template <class T>
std::string to_string_slow(T t) {
    std::string res;

    do {
        res += '0' + t % 10;
        t /= 10;
    } while (t);

    return reversed(res);
}

void out(std::ostream& o, ui128 v) {
    o << to_string_slow(v);
}

void out(std::ostream& o, i128 v) {
    if (v < 0) {
        out(o << "-", (ui128)(-v));
    } else {
        out(o, (ui128)v);
    }
}
