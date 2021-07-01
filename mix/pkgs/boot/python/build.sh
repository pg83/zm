$untar $src/Python* && cd Python*

setup_compiler

dash ./configure --prefix=$out --enable-static --disable-shared --with-ensurepip=no
make -j $make_thrs
make install
