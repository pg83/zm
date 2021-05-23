$untar $src/sed-* && cd sed-*

dash ./configure --prefix=$out
make -j $make_thrs
make install
