$untar $src/cmake* && cd cmake*

export CFLAGS="-w $CPPFLAGS $CFLAGS $LDFLAGS $LIBS"
export CXXFLAGS="-w $CPPFLAGS $CXXFLAGS $LDFLAGS $LIBS"

dash ./bootstrap --prefix=$out --parallel=8 -- -DCMAKE_USE_OPENSSL=OFF -Dfortran=OFF -DBUILD_TESTING=OFF

echo > .clang-tidy

./Bootstrap.cmk/cmake .

make -j 8
make install
