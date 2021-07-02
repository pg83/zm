# url http://gondor.apana.org.au/~herbert/dash/files/dash-0.5.11.3.tar.gz
# md5 c7016b513f701d88c70b3082eb183581
# dep boot/which boot/autohell boot/coreutils boot/bin/stdenv env/compiler

build() {
    $untar $src/dash-* && cd dash-*

    setup_compiler

    dash ./configure --prefix=$out
    make -j $make_thrs
    make install
}
