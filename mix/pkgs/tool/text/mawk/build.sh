$untar $src/mawk* && cd mawk*

dash ./configure $COFLAGS --prefix=$out
make -j $make_thrs
make install
