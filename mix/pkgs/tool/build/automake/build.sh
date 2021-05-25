$untar $src/automake* && cd automake*

dash ./configure --prefix=$out
make -j $make_thrs
make install
