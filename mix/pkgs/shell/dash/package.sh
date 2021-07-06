# url http://gondor.apana.org.au/~herbert/dash/files/dash-0.5.11.3.tar.gz
# md5 c7016b513f701d88c70b3082eb183581
# dep lib/intl lib/edit lib/iconv dev/build/make dev/build/pkg-config env/compiler stdenv

build() {
    $untar $src/dash-* && cd dash-*

    setup_compiler

    dash ./configure $(echo $COFLAGS | tr ' ' '\n' | grep -v libedit | tr ' ' '\n') --with-libedit=yes --prefix=$out
    make -j $make_thrs
    make install
}
