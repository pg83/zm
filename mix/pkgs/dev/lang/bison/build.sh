$untar $src/bison* && cd bison*

dash ./configure $COFLAGS --prefix=$out --enable-relocatable
make -j $make_thrs
make install
