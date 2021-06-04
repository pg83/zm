$untar $src/autoconf* && cd autoconf*

dash ./configure $COFLAGS --prefix=$out
make -j $make_thrs
make install
