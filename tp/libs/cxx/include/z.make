module: library

global_inc_dirs:
- tp/libs/cxx/include

inc_dirs:
- tp/libs/unwind/include

#if MUSL
depends:
- tp/libs/muslinc
#endif

srcs:
- all.cpp
