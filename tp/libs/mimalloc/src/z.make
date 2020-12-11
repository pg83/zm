module: object

c_flags:
#if OS_DARWIN
- -DMI_OSX_ZONE=1
#endif
- -DMI_INTERPOSE
- -DMI_MALLOC_OVERRIDE
- -DMI_STATIC_LIB

inc_dirs:
- tp/libs/mimalloc/include

join_srcs:
- empty.cpp
#if OS_DARWIN
- alloc-override-osx.c
#endif
- alloc-aligned.c
- alloc-posix.c
- alloc.c
- arena.c
- heap.c
- init.c
- options.c
- os.c
- page.c
- random.c
- region.c
- segment.c
- stats.c
