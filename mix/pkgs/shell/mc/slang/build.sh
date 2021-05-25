$untar $src/mc* && cd mc*

export LDFLAGS="$LDFLAGS $LIBS"

dash ./configure $COFLAGS --prefix=$out --disable-shared --enable-static --with-screen=slang

make -j $make_thrs
echo 'all install:' > doc/hlp/Makefile
make install
