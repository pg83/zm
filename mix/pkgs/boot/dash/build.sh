$untar $src/dash-* && cd dash-*

export CFLAGS_FOR_BUILD="$CPPFLAGS $CFLAGS $LDFLAGS $LIBS"

dash ./configure --prefix=$out
make -j $make_thrs
make install
