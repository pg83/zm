module: library

cxx_flags:
- -D_LIBCXXABI_DISABLE_VISIBILITY_ANNOTATIONS

srcs:
- cxa_demangle.cpp

depends:
- third_party/libs/libcxx/include

inc_dirs:
- third_party/libs/libdemange/demangle
