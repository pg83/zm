module: program

inc_dirs:
- third_party/tools/gperf

c_flags:
- -w

join_srcs:
- getline.cpp
- hash.cpp
- keyword.cpp
- main.cpp
- options.cpp
- output.cpp
- search.cpp
- version.cpp
- hash-table.cpp
- bool-array.cpp
- input.cpp
- keyword-list.cpp
- positions.cpp

srcs:
- getopt.c
- getopt1.c
