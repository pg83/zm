module: program

srcs:
- main.cpp
- data.file2c

ld_flags:
- -nostdlib++

depends:
- libs/lib1
- third_party/libs/libcxxrt
