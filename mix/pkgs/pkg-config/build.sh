$untar $src/pkg* && cd pkg*

export LDFLAGS="$LDFLAGS $LIBS"
export GLIB_LIBS="$LIBS"

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
make -j $make_thrs
make install
