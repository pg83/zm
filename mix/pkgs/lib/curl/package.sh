# url https://github.com/curl/curl/releases/download/curl-7_76_1/curl-7.76.1.tar.xz
# md5 5296108646ca7f318b468a7a9d4a0eb2
# lib lib/z lib/idn2 lib/zstd lib/brotli lib/nghttp2 lib/openssl
# dep dev/build/make dev/build/pkg-config stdenv

build() {
    $untar $src/curl* && cd curl*

    export LIBS=$(echo "$LDFLAGS" | tr ' ' '\n' | grep '^-l' | tr '\n' ' ')

    dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
    make -j $make_thrs
    make install

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lcurl \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
export CMFLAGS="-DCURL_LIBRARY=$out/lib/libcurl.a -DCURL_INCLUDE_DIR=$out/include \$CMFLAGS"
EOF
}
