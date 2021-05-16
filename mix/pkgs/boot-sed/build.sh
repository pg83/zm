$untar $src/sed-* && cd sed-*

dash ./configure --prefix=$out
make
make install
