$untar $src/Python* && cd Python*

export MACOSX_DEPLOYMENT_TARGET=10.6
export CFLAGS="$CPPFLAGS $CFLAGS"
export CXXFLAGS="$CPPFLAGS $CXXFLAGS"

dash ./configure --prefix=$out --enable-static --disable-shared --with-ensurepip=no
make -j 8
make install
