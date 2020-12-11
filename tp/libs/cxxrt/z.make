module: library

depends:
- tp/libs/unwind
- tp/libs/demangle
- tp/libs/cxx/include

inc_dirs:
- tp/libs/cxxrt

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
