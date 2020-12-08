module: library

global_inc_dirs:
- tp/libs/libcxx/include

inc_dirs:
- tp/libs/libunwind/include

#if OS_LINUX
depends:
- tp/libs/libmuslinc
#endif

srcs:
- all.cpp
