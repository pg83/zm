# url https://pkg-config.freedesktop.org/releases/pkg-config-0.29.2.tar.gz
# md5 f6e931e319531b736fadc017f470e68a
# dep lib/glib lib/iconv dev/build/make boot/pkg-config env/compiler stdenv

build() {
    $untar $src/pkg* && cd pkg*

    ln -s $(which dash) sh
    export PATH="$(pwd):$PATH"

    setup_compiler

    dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared --disable-host-tool
    make -j $make_thrs
    make install

    cat << EOF > $out/env
export PKG_CONFIG="$out/bin/pkg-config"
EOF
}
