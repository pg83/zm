# url https://pkg-config.freedesktop.org/releases/pkg-config-0.29.2.tar.gz
# md5 f6e931e319531b736fadc017f470e68a
# dep boot/iconv boot/which boot/autohell boot/diffutils boot/findutils boot/coreutils boot/bin/stdenv env/compiler

build() {
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
}
