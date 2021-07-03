# url https://ftpmirror.gnu.org/libtool/libtool-2.4.6.tar.gz
# md5 addf44b646ddb4e3919805aa88fa7c5e
# dep dev/lang/m4 dev/build/make stdenv

build() {
    $untar $src/libtool* && cd libtool*

    dash ./configure $COFLAGS --prefix=$out
    make -j $make_thrs
    make install
}
