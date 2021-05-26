$untar $src/help* && cd help*

dash ./configure --prefix=$out
make -j $make_thrs
make install
