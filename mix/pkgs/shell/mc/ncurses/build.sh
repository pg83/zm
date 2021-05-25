$untar $src/mc* && cd mc*

export CPPFLAGS="-DNCURSES_WIDECHAR $CPPFLAGS"
export LDFLAGS="$LDFLAGS $LIBS"

dash ./configure $COFLAGS --prefix=$out --disable-shared --enable-static --with-screen=ncurses

make -j $make_thrs
echo 'all install:' > doc/hlp/Makefile
make install
