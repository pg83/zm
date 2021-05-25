$untar $src/which* && cd which*

dash ./configure --prefix=$out
make -j $make_thrs
make install
