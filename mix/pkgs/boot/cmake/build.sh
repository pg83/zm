$untar $src/cmake* && cd cmake*

setup_compiler
build_cmake_ps

dash ./bootstrap --prefix=$out --parallel=$make_thrs -- -DCMAKE_USE_OPENSSL=OFF -Dfortran=OFF -DBUILD_TESTING=OFF
make -j $make_thrs
make install
