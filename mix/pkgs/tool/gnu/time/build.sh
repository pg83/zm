$untar $src/time* && cd time*

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
make -j $make_thrs
make install
