$untar $src/help* && cd help*

dash ./configure $COFLAGS --prefix=$out
make -j $make_thrs
make install
