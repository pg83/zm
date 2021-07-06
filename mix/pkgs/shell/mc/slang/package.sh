# url http://ftp.midnight-commander.org/mc-4.8.26.tar.xz
# md5 3c1f77b71dba1f4eeeedc4276627fed7
# dep lib/intl lib/glib lib/pcre lib/iconv lib/slang dev/build/make dev/build/pkg-config env/compiler stdenv

build() {
    $untar $src/mc* && cd mc*

    setup_compiler

    dash ./configure $COFLAGS \
        --prefix=$out \
        --disable-shared \
        --enable-static \
        --with-screen=slang \
        --with-search-engine=pcre

    make -j $make_thrs
    make install
}
