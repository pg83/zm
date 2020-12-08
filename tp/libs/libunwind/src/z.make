module: library

global_inc_dirs:
- tp/libs/libunwind/include

inc_dirs:
- tp/libs/libunwind/src

depends:
- tp/libs/libcxx/include

c_flags:
- -D_LIBUNWIND_IS_NATIVE_ONLY
- -fno-exceptions
- -fno-rtti
- -funwind-tables
- -w

srcs:
#if OS_DARWIN
- Unwind_AppleExtras.cpp
#endif
- Unwind-EHABI.cpp
- Unwind-seh.cpp
- Unwind-sjlj.c
- UnwindLevel1-gcc-ext.c
- UnwindLevel1.c
- UnwindRegistersRestore.S
- UnwindRegistersSave.S
- libunwind.cpp
