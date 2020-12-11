module: library

inc_dirs:
- tp/libs/cxxrt
- tp/libs/cxx/src/include
- tp/libs/cxx/src/support/runtime

depends:
- tp/libs/cxx/include
- tp/libs/cxxrt

cxx_flags:
- -D_LIBCPP_BUILDING_LIBRARY
- -D_LIBCPP_PROVIDES_DEFAULT_RUNE_TABLE
- -DLIBCXXRT=1

srcs:
- algorithm.cpp
- any.cpp
- bind.cpp
- charconv.cpp
- chrono.cpp
- condition_variable.cpp
- exception.cpp
- functional.cpp
- future.cpp
- hash.cpp
- ios.cpp
- locale.cpp
- memory.cpp
- mutex.cpp
- optional.cpp
- random.cpp
- regex.cpp
- shared_mutex.cpp
- stdexcept.cpp
- string.cpp
- strstream.cpp
- system_error.cpp
- thread.cpp
- typeinfo.cpp
- utility.cpp
- valarray.cpp
- variant.cpp
- vector.cpp
- new.cpp
- debug.cpp
- condition_variable_destructor.cpp
- iostream.cpp
- mutex_destructor.cpp
