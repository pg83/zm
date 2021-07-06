# url https://ftp.gnu.org/gnu/termcap/termcap-1.3.1.tar.gz
# md5 ffe6f86e63a3a29fa53ac645faaabdfa
# dep dev/build/make stdenv

build() {
    $untar $src/termcap* && cd termcap*

    dash ./configure $COFLAGS --prefix=$out --disable-shared --enable-static
    make -j $make_thrs
    make install

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -ltermcap \$LDFLAGS"
EOF
}
