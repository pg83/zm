# url https://github.com/jtanx/libclipboard/archive/refs/tags/v1.1.tar.gz
# md5 bddc22070b6804ed63994af49b778b70
# dep dev/build/cmake dev/build/pkg-config stdenv

build() {
    $untar $src/v* && cd lib*

    build_cmake_ninja ..

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-framework AppKit -L$out/lib -lclipboard \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
}
