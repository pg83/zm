# url https://github.com/Kitware/CMake/releases/download/v3.20.2/cmake-3.20.2.tar.gz
# md5 cd0e7735f1e51f30ee3b0844390a464a
# lib dev/build/ninja
# dep lib/z lib/xz lib/uv lib/cxx lib/curl lib/bzip2 lib/expat lib/archive boot/cmake boot/pkg-config stdenv
# run env/cmake

build() {
    $untar $src/cmake* && cd cmake*

    build_cmake_ninja \
        -Dfortran=OFF \
        -DBUILD_TESTING=OFF \
        -DCMAKE_USE_SYSTEM_CURL=ON \
        -DCMAKE_USE_SYSTEM_BZIP2=ON \
        -DCMAKE_USE_SYSTEM_LIBLZMA=ON \
        ..
}
