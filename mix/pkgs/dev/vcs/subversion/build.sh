$untar $src/sub* && cd sub*

export COFLAGS=$(echo "$COFLAGS" | tr ' ' '\n' | grep -v expat | tr '\n' ' ')
export COFLAGS="$COFLAGS --with-expat=$lib_expat/include:$lib_expat/lib:-lexpat"

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
make -j $make_thrs
make install
