$untar $src/patch* && cd patch*

./configure $COFLAGS --prefix=$out
make -j $make_thrs
make install
