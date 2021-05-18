$untar $src/which* && cd which*

dash ./configure --prefix=$out
make
make install
