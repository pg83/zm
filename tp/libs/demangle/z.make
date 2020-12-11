module: library

cxx_flags:
- -D_LIBCXXABI_DISABLE_VISIBILITY_ANNOTATIONS

srcs:
- cxa_demangle.cpp

depends:
- tp/libs/cxx/include

inc_dirs:
- tp/libs/demangle/demangle
- tp/libs/demangle
