$untar $src/find* && cd find*

(cd gl/lib/malloc && echo '#define __nonnull(x)' > tmp && cat dynarray-skeleton.c >> tmp && mv tmp dynarray-skeleton.c)

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
make -j $make_thrs
make install
