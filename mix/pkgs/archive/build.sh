$untar $src/lib* && cd lib*

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared --without-xml2 --without-expat
make -j $make_thrs
make install
