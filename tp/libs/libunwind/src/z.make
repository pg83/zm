module: library

global_inc_dirs:
- tp/libs/libunwind/include

inc_dirs:
- tp/libs/libunwind/src

c_flags:
- -D_LIBUNWIND_IS_NATIVE_ONLY
- -fno-exceptions
- -fno-rtti
- -funwind-tables
- -w

srcs:
- Unwind-EHABI.cpp
- Unwind-seh.cpp
- Unwind-sjlj.c
- UnwindLevel1-gcc-ext.c
- UnwindLevel1.c
- UnwindRegistersRestore.S
- UnwindRegistersSave.S
- libunwind.cpp
- Unwind_AppleExtras.cpp
