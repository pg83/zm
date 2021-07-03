# url https://ftp.gnu.org/gnu/sed/sed-4.8.tar.xz
# md5 6d906edfdb3202304059233f51f9a71d
# dep boot/make boot/coreutils boot/heirloom boot/bin/stdenv

build() {
    $untar $src/sed-* && cd sed-*

    dash ./configure --prefix=$out
    make -j $make_thrs
    make install
}
