module: library

cxx_flags:
- -D_LIBCXXABI_DISABLE_VISIBILITY_ANNOTATIONS

srcs:
- cxa_demangle.cpp

depends:
- tp/libs/libcxx/include

inc_dirs:
- tp/libs/libdemangle/demangle
- tp/libs/libdemangle
