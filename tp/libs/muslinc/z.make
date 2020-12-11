module: library

global_inc_dirs:
- tp/libs/musl/arch/x86_64
- tp/libs/musl/arch/generic
- tp/libs/musl/include
- tp/libs/musl/extra

depends:
- tp/libs/musl

srcs:
- dlvsym.cpp
