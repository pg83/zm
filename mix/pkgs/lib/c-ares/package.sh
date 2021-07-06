# url https://c-ares.haxx.se/download/c-ares-1.17.1.tar.gz
# md5 28f65c8ee6c097986bd902fd4f0804e2
# dep dev/build/make stdenv

build() {
    $untar $src/c* && cd c*

    dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared --disable-tests
    make -j $make_thrs
    make install

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lcares \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
}
