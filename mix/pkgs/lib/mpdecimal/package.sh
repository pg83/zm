# url https://www.bytereef.org/software/mpdecimal/releases/mpdecimal-2.5.1.tar.gz
# md5 18599e4ffcfe8cd93e0efa8f14f027eb
# dep dev/build/make env/compiler stdenv

build() {
    $untar $src/mpdecimal* && cd mpdecimal*

    setup_compiler

    dash ./configure $COFLAGS --prefix=$out --disable-shared --enable-static --enable-cxx=no
    make -j $make_thrs
    make install

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lmpdec \$LDFLAGS"
EOF
}
