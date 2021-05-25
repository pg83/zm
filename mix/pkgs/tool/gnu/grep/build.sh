$untar $src/grep-* && cd grep-*

dash ./configure $COFLAGS --prefix=$out
make -j $make_thrs
make install
