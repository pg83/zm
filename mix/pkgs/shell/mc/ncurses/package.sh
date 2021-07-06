# url http://ftp.midnight-commander.org/mc-4.8.26.tar.xz
# md5 3c1f77b71dba1f4eeeedc4276627fed7
# dep lib/intl lib/glib lib/iconv lib/ncurses dev/build/make dev/build/pkg-config stdenv

build() {
    $untar $src/mc* && cd mc*

    export CPPFLAGS="-DNCURSES_WIDECHAR $CPPFLAGS"
    export LDFLAGS="$LDFLAGS $LIBS"

    dash ./configure $COFLAGS --prefix=$out --disable-shared --enable-static --with-screen=ncurses

    make -j $make_thrs
    echo 'all install:' > doc/hlp/Makefile
    make install
}
