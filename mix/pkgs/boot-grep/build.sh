$untar $src/grep-* && cd grep-*

dash ./configure --prefix=$out
make
make install
