module: library

inc_dirs:
- tp/libs/libcxxrt

depends:
- tp/libs/libcxx/include
- tp/libs/libcxxrt

cxx_flags:
- -D_LIBCPP_BUILDING_LIBRARY
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
