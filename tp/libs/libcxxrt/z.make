module: library

depends:
- tp/libs/libunwind
- tp/libs/libdemangle
- tp/libs/libcxx/include

inc_dirs:
- tp/libs/libcxxrt

cxx_flags:
- -w

srcs:
- memory.cc
- auxhelper.cc
- stdexcept.cc
- exception.cc
- guard.cc
- typeinfo.cc
- dynamic_cast.cc
- unwind.cc
