$untar $src/bison* && cd bison*

dash ./configure $COFLAGS --prefix=$out --enable-relocatable

(
    cd src

    rm parse-gram.c parse-gram.h
    cat parse-gram.y | grep -v 'define api.token.raw' > qw && mv qw parse-gram.y
    bison parse-gram.y
    mv parse-gram.tab.c parse-gram.c && mv parse-gram.tab.h parse-gram.h
)

make -j $make_thrs
make install
