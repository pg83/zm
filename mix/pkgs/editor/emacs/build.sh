$untar $src/emacs* && cd emacs*

dash ./configure $COFLAGS \
     --prefix=$out \
     --enable-static \
     --disable-shared \
     --without-all \
     --without-x \
     --with-dumping=pdumper \
     --without-ns

make -j $make_thrs
make install
