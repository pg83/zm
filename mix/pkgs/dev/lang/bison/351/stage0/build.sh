$untar $src/bison* && cd bison*

dash ./configure $COFLAGS --prefix=$out --enable-relocatable

# 1
(
    cd src

    cp parse-gram.y orig.y

    rm parse-gram.c parse-gram.h
    cat orig.y | grep -v 'define api.token.raw' > parse-gram.y
    bison parse-gram.y
    mv parse-gram.tab.c parse-gram.c && mv parse-gram.tab.h parse-gram.h
)

rm -rf $out && make -j $make_thrs
make install

# 2
(
    cd src

    rm parse-gram.c parse-gram.h
    mv orig.y parse-gram.y
    ./bison parse-gram.y
    mv parse-gram.tab.c parse-gram.c && mv parse-gram.tab.h parse-gram.h
)

rm -rf $out && make -j $make_thrs
make install
