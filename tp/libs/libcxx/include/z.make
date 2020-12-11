module: library

global_inc_dirs:
- tp/libs/libcxx/include

inc_dirs:
- tp/libs/libunwind/include

#if MUSL
depends:
- tp/libs/libmuslinc
#endif

srcs:
- all.cpp
