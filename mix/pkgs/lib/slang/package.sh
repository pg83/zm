# url https://storage.yandexcloud.net/mix-cache/slang-2.3.2.tar.bz2
# md5 c2d5a7aa0246627da490be4e399c87cb
# lib lib/z lib/pcre lib/iconv lib/readline
# dep dev/build/make stdenv

build() {
    $untar $src/slang* && cd slang*

    export AR_CR="ar cr"
    export CFLAGS="$CPPFLAGS $CFLAGS"

    dash ./configure $COFLAGS \
        --disable-shared \
        --enable-static \
        --prefix=$out \
        --with-readline=gnu \
        --without-png \
        --without-onig

    make AR_CR="$AR_CR" CFLAGS="$CFLAGS" install-static

    cat << EOF > $out/env
export SLANG_CFLAGS="-I$out/include"
export SLANG_LIBS="-L$out/lib -lslang"
export CPPFLAGS="\$SLANG_CFLAGS \$CPPFLAGS"
export LDFLAGS="\$SLANG_LIBS \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
}
