. $bin_stdenv/env

$exe $mix misc untar $src/sed-* && cd sed-*

dash ./configure --prefix=$out
make
make install
