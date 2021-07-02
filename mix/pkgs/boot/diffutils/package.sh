# url https://ftp.gnu.org/gnu/diffutils/diffutils-3.7.tar.xz
# md5 4824adc0e95dbbf11dfbdfaad6a1e461
# dep boot/autohell boot/coreutils boot/bin/stdenv

build() {
    $untar $src/diffutils-* && cd diffutils-*

    dash ./configure --prefix="$out" --disable-gcc-warnings

    echo 'all install:' > man/Makefile

    make -j $make_thrs
    make install
}
