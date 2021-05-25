$untar $src/grep-* && cd grep-*

dash ./configure --prefix=$out
make -j $make_thrs
make install
