# url https://gmplib.org/download/gmp/gmp-6.2.1.tar.lz
# md5 03a31d8cbaf29d136252f8f38875ed82
# dep dev/build/make dev/lang/m4 stdenv

build() {
    $untar $src/gmp* && cd gmp*

    dash ./configure $COFLAGS --prefix="$out" --enable-static --disable-shared
    make -j $make_thrs
    make install

    cat << EOF > $out/env
export COFLAGS="--with-gmp=$out \$COFLAGS"
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lgmp \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
}
