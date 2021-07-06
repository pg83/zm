# url https://ftp.gnu.org/gnu/libidn/libidn2-2.3.1.tar.gz
# md5 cda07f5ac55fccfafdf7ee01828adad5
# lib lib/intl lib/iconv lib/unistring
# dep dev/build/make dev/build/pkg-config stdenv

build() {
    $untar $src/libidn2* && cd libidn2*

    dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
    make -j $make_thrs
    make install

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lidn2 \$LDFLAGS"
export COFLAGS="--with-libidn2=$out \$COFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
}
