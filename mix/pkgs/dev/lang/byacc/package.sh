# url https://invisible-island.net/datafiles/release/byacc.tar.gz
# md5 ad027e9a1a78666e3e27924ce6854f97
# dep dev/build/make stdenv

build() {
    $untar $src/byacc* && cd byacc*

    dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
    make -j $make_thrs
    make install
}
