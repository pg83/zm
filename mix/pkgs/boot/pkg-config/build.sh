$untar $src/pkg* && cd pkg*

export GLIB_LIBS="$LIBS"

setup_compiler

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared --with-internal-glib --disable-host-tool

(
    cd glib
    dash ./configure $COFLAGS --prefix=$out --with-libiconv=gnu --enable-static --disable-shared --srcdir=.
    make -j $make_thrs
)

make -j $make_thrs
make install
