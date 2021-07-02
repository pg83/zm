# url https://github.com/Kitware/CMake/releases/download/v3.20.2/cmake-3.20.2.tar.gz
# md5 cd0e7735f1e51f30ee3b0844390a464a
# dep env/cmake boot/which boot/libcxx boot/autohell boot/coreutils boot/bin/stdenv env/compiler
# run env/cmake

build() {
    $untar $src/cmake* && cd cmake*

    setup_compiler
    build_cmake_ps

    dash ./bootstrap --prefix=$out --parallel=$make_thrs -- -DCMAKE_USE_OPENSSL=OFF -Dfortran=OFF -DBUILD_TESTING=OFF
    make -j $make_thrs
    make install
}
