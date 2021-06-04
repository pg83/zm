$untar $src/automake* && cd automake*

dash ./configure $COFLAGS --prefix=$out
make -j $make_thrs
make install
