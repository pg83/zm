module: object

c_flags:
- -DMI_INTERPOSE
- -DMI_MALLOC_OVERRIDE
- -DMI_OSX_ZONE=1
- -DMI_STATIC_LIB

inc_dirs:
- tp/libs/libmimalloc/include

join_srcs:
- alloc-aligned.c
- alloc-override-osx.c
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
