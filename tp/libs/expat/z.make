module: library

c_flags:
- -DXML_POOR_ENTROPY=1
- -w

srcs:
- xmlparse.c
- xmlrole.c
- xmltok.c
- xmltok_impl.c
- xmltok_ns.c
