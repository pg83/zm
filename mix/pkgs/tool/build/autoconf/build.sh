$untar $src/autoconf* && cd autoconf*

dash ./configure --prefix=$out
make -j $make_thrs
make install
