#pragma once

#define Z_CAT(X, Y) Z_CAT_I(X, Y)
#define Z_CAT_I(X, Y) Z_CAT_II(X, Y)
#define Z_CAT_II(X, Y) X##Y

#if defined(__COUNTER__)
    #define Z_GENERATE_UNIQUE_ID(N) Z_CAT(N, __COUNTER__)
#endif

#if !defined(Z_GENERATE_UNIQUE_ID)
    #define Z_GENERATE_UNIQUE_ID(N) Z_CAT(N, __LINE__)
#endif
