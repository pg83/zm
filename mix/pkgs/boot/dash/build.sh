$untar $src/dash-* && cd dash-*

setup_compiler

dash ./configure --prefix=$out
make -j $make_thrs
make install
