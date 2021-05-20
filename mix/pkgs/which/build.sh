$untar $src/which* && cd which*

dash ./configure $COFLAGS --prefix=$out
make -j $make_thrs
make install
