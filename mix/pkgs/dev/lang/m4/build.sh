$untar $src/m4* && cd m4*

patch -p0 < $src/secure_snprintf.patch

dash ./configure $COFLAGS --prefix=$out --disable-c++
make -j $make_thrs
make install
