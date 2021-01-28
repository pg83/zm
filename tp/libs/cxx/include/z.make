module: library

global_inc_dirs:
- tp/libs/cxx/include

inc_dirs:
- tp/libs/unwind/include

#if MUSL
depends:
- tp/libs/muslinc
#endif

#if not MUSL and OS_LINUX
ld_flags:
- -lc
- -ldl
- -lpthread
#endif

srcs:
- all.cpp
