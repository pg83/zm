$untar $src/libtool* && cd libtool*

dash ./configure $COFLAGS --prefix=$out
make -j $make_thrs
make install
