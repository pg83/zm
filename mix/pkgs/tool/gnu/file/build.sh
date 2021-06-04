$untar $src/file* && cd file*

./configure $COFLAGS --prefix=$out --enable-static --disable-shared
make -j $make_thrs
make install
