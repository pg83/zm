$untar $src/bison* && cd bison*

export BISON=$(which bison)

dash ./configure $COFLAGS --prefix=$out --enable-relocatable
rm src/parse-gram.c src/parse-gram.h
make src/parse-gram.c
make -j $make_thrs
make install
