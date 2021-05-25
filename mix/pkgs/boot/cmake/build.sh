$untar $src/cmake* && cd cmake*

export CFLAGS="-w $CPPFLAGS $CFLAGS $LDFLAGS $LIBS"
export CXXFLAGS="-w $CPPFLAGS $CXXFLAGS $LDFLAGS $LIBS"

dash ./bootstrap --prefix=$out --parallel=$make_thrs -- -DCMAKE_USE_OPENSSL=OFF -Dfortran=OFF -DBUILD_TESTING=OFF
make -j $make_thrs
make install
