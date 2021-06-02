$untar $src/cmake* && cd cmake*

build_cmake_ninja \
    -Dfortran=OFF \
    -DBUILD_TESTING=OFF \
    -DCMAKE_USE_SYSTEM_CURL=ON \
    -DCMAKE_USE_SYSTEM_BZIP2=ON \
    -DCMAKE_USE_SYSTEM_LIBLZMA=ON \
    ..
