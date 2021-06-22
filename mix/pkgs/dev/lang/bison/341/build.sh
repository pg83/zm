$untar $src/bison-3* && cd bison* && $untar $src/bison-b* && ln -s bison-b* bb

cp src/parse-gram.y parse-gram.y.orig
cp bb/parse-gram.y src/
cp bb/parse-gram.c bb/parse-gram.h src/

dash ./configure $COFLAGS --prefix=$out --enable-relocatable

make

touch src/parse-gram.y && rm src/parse-gram.c src/parse-gram.h

make

cp parse-gram.y.orig src/parse-gram.y && rm src/parse-gram.c src/parse-gram.h

make
make install
