$untar $src/gzip* && cd gzip*

dash ./configure $COFLAGS --prefix=$out --disable-gcc-warnings
make -j $make_thrs
make install
