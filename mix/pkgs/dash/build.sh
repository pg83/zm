export CFLAGS_FOR_BUILD="$CPPFLAGS $CFLAGS $LDFLAGS $LIBS"

$untar $src/dash-* && cd dash-*

dash ./configure $COFLAGS --prefix=$out
make -j $make_thrs
make install
