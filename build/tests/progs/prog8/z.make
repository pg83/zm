module: program

resource:
- file1 file1
- file2 tmp/file2

srcs:
- main.cpp

depends:
- libs/resource
