$untar $src/cmake* && cd cmake*

export CPPFLAGS="-w $CPPFLAGS"

build_cmake_ninja -DCMAKE_USE_OPENSSL=OFF -Dfortran=OFF -DBUILD_TESTING=OFF ..
