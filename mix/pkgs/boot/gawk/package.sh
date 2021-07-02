# url https://mirror.tochlab.net/pub/gnu/gawk/gawk-5.1.0.tar.xz
# md5 8470c34eeecc41c1aa0c5d89e630df50
# dep boot/sed boot/grep boot/make boot/coreutils boot/heirloom boot/bin/stdenv

build() {
    $untar $src/gawk-* && cd gawk-*

    export CFLAGS="-Derr=gawk_err -Dxmalloc=gawk_xmalloc -Dxrealloc=Dgawk_xrealloc -Dregcomp=gawk_regcomp -Dregfree=gawk_regfree $CFLAGS"

    dash ./configure --prefix=$out --libexecdir=$out/bin/awk_exec --disable-shared --enable-static --disable-extensions
    make -j $make_thrs
    make install
}
