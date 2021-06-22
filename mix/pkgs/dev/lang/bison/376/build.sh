$untar $src/bison* && cd bison*

dash ./configure $COFLAGS --prefix=$out --enable-relocatable

rm src/parse-gram.c src/parse-gram.h
bison src/parse-gram.y
mv parse-gram.tab.c src/parse-gram.c
mv parse-gram.tab.h src/parse-gram.h

make -j $make_thrs
make install

rm src/parse-gram.c src/parse-gram.h
./src/bison src/parse-gram.y
mv parse-gram.tab.c src/parse-gram.c
mv parse-gram.tab.h src/parse-gram.h

rf -rf $out && make -j $make_thrs
make install
