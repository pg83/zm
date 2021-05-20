$untar $src/sed-* && cd sed-*

dash ./configure $COFLAGS --prefix=$out
make -j $make_thrs
make install
