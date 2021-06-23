$untar $src/flex* && cd flex*

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared

(
    cd src

    rm parse.c parse.h
    yacc -d parse.y && mv y.tab.c parse.c && mv y.tab.h parse.h
    echo 'extern int yylval;' >> parse.h
)

make -j $make_thrs
make install
