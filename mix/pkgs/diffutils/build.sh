$untar $src/diffutils-* && cd diffutils-*

dash ./configure $COFLAGS --prefix=$out --disable-gcc-warnings

echo 'all install:' > man/Makefile

make -j $make_thrs
make install
