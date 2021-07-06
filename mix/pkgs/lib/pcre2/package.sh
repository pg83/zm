# url https://ftp.pcre.org/pub/pcre/pcre2-10.36.tar.gz
# md5 a5d9aa7d18b61b0226696510e60c9582
# dep lib/z lib/bzip2 dev/build/make boot/pkg-config stdenv

build() {
    $untar $src/pcre* && cd pcre*

    dash ./configure $COFLAGS \
        --prefix=$out \
        --disable-shared \
        --enable-static \
        --enable-pcre2grep-libz \
        --enable-pcre2grep-libbz2 \
        --enable-newline-is-anycrlf \
        --enable-utf8 \
        --enable-jit \
        --enable-c++

    make -j $make_thrs
    make install

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lpcre2-8 \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
}
