module: library

depends:
- third_party/libs/libunwind
- third_party/libs/libdemangle

inc_dirs:
- third_party/libs/libcxxrt

cxx_flags:
- -nostdinc++
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
