# url https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tar.xz
# md5 71f7ada6bec9cdbf4538adc326120cfd
# dep boot/which boot/autohell boot/coreutils boot/bin/stdenv boot/compiler_rt env/compiler

build() {
    $untar $src/Python* && cd Python*

    setup_compiler

    dash ./configure --prefix=$out --enable-static --disable-shared --with-ensurepip=no
    make -j $make_thrs
    make install
}
