# url https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.2.tar.gz
# md5 e812da327b1c2214ac1aed440ea3ae8d
# dep boot/pkg-config dev/build/make stdenv

build() {
    $untar $src/ncurses* && cd ncurses*

    dash ./configure $COFLAGS \
        --prefix=$out \
        --without-shared \
        --without-debug \
        --without-ada \
        --enable-widec \
        --enable-pc-files \
        --enable-overwrite \
        --enable-ext-colors \
        --enable-termcap \
        --with-pkg-config \
        --with-termlib \
        --without-cxx \
        --without-cxx-binding

    make -j $make_thrs
    make install

    cd $out/lib && (for i in `ls *.a`; do q=`echo $i | tr -d 'w'`; ln -s $i $q; done)

    cat << EOF > $out/env
export COFLAGS="--with-curses=$out --with-ncurses=$out \$COFLAGS"
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lncurses -ltinfo -lpanel -lmenu -lform \$LDFLAGS"
EOF
}
