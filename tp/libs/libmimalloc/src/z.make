module: object

c_flags:
#if OS_DARWIN
- -DMI_OSX_ZONE=1
#endif
- -DMI_INTERPOSE
- -DMI_MALLOC_OVERRIDE
- -DMI_STATIC_LIB

inc_dirs:
- tp/libs/libmimalloc/include

srcs:
- all.cpp
