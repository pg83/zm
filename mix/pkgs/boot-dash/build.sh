. $bin_stdenv/env

export CFLAGS_FOR_BUILD="$CPPFLAGS $CFLAGS $LDFLAGS $LIBS"

$exe $mix misc untar $src/dash-* && cd dash-*

dash ./configure --prefix=$out
make
make install
