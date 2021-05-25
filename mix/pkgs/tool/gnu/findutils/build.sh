$untar $src/find* && cd find*

echo '#define __nonnull(x)' > tmp
cat gl/lib/malloc/dynarray-skeleton.c >> tmp
mv tmp gl/lib/malloc/dynarray-skeleton.c

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
make -j $make_thrs
make install
