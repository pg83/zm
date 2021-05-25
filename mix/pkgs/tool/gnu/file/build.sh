$untar $src/file* && cd file*

./configure --prefix=$out --enable-static --disable-shared
make -j $make_thrs
make install
