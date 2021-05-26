$untar $src/libtool* && cd libtool*

dash ./configure --prefix=$out
make -j $make_thrs
make install
