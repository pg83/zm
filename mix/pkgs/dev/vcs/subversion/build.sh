$untar $src/sub* && cd sub*

dash ./configure --prefix=$out --enable-static --disable-shared
make -j $make_thrs
make install
