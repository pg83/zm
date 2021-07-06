# url https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz
# md5 3bcd2441024d00009a5fee43f058987c
# dep lib/z lib/bzip2 dev/build/make boot/pkg-config stdenv

build() {
    $untar $src/pcre* && cd pcre*

    dash ./configure $COFLAGS \
        --prefix=$out \
        --disable-shared \
        --enable-static \
        --enable-pcregrep-libz \
        --enable-pcregrep-libbz2 \
        --enable-unicode-properties \
        --enable-pcre16 \
        --enable-pcre32 \
        --enable-jit \
        --disable-cpp

    make -j $make_thrs
    make install

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lpcre \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
export COFLAGS="--with-pcre=$out \$COFLAGS"
export CMFLAGS="-DPCRE_LIBRARY=$out/lib/libpcre.a -DPCRE_INCLUDE_DIR=$out/include \$CMFLAGS"
EOF
}
