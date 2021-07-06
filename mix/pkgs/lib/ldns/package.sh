# url https://nlnetlabs.nl/downloads/ldns/ldns-1.7.1.tar.gz
# md5 166262a46995d9972aba417fd091acd5
# lib lib/openssl
# dep dev/build/make stdenv

build() {
    $untar $src/ldns* && cd ldns*

    ln -s $(which dash) sh
    export PATH="$(pwd):$PATH"

    dash ./configure $COFLAGS \
        --prefix=$out \
        --enable-static \
        --disable-shared \
        --with-ssl=$lib_openssl \
        --with-drill

    make -j $make_thrs
    make install

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lldns \$LDFLAGS"
export COFLAGS="--with-ldns=$out \$COFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
}
