# url https://github.com/facebook/zstd/releases/download/v1.5.0/zstd-1.5.0.tar.gz
# md5 a6eb7fb1f2c21fa80030a47993853e92
# dep dev/build/make stdenv/tiny

build() {
    $untar $src/zstd* && cd zstd*

    make PREFIX=$out CC=gcc CXX=g++ -j $make_thrs install

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lzstd \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
}
