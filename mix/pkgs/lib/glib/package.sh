# url https://download-fallback.gnome.org/sources/glib/2.68/glib-2.68.2.tar.xz
# md5 8d288416da38476c71998e5c2d3602ed
# lib lib/z lib/pcre lib/iconv lib/ffi lib/intl
# dep dev/build/meson dev/build/ninja boot/pkg-config env/compiler stdenv

build() {
    $untar $src/glib* && cd glib*

    export CPPFLAGS="-D_GNU_SOURCE=1 -I$(pwd)/inc $CPPFLAGS"

    setup_compiler

    echo 'int main() {}' > glib/tests/cxx.cpp
    echo 'int main() {}' > tests/cxx-test.cpp

    meson -Ddefault_library=static -Dprefix=$out _build && cd _build

    ninja -j $make_thrs
    ninja install

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -framework CoreServices -framework Foundation -lglib-2.0 -lgobject-2.0 -lgio-2.0 -lgmodule-2.0 -lgthread-2.0 \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
}
