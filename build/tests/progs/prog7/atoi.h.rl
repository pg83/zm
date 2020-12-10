#pragma once

#include <build/tests/progs/prog7/inc.h>

%%{
    machine ParseStreamUnsigned;
    write data;
}%%

template <class T, class It>
static inline bool parse_stream_unsigned(T& val, It p, It pe) {
    int cs;
    val = 0;

    if (p == pe) {
        return false;
    }

    %%{
        action add_digit {
            val = val * 10 + (fc - '0');
        }

        main := ('+')? (digit @add_digit)+;

        write init;
        write exec;
    }%%

    return cs < ParseStreamUnsigned_first_final;
}
