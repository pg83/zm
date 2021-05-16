export CFLAGS_FOR_BUILD="$CPPFLAGS $CFLAGS $LDFLAGS $LIBS"

$untar $src/dash-* && cd dash-*

dash ./configure --prefix=$out
make
make install
