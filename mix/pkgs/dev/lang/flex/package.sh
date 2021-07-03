# url https://github.com/westes/flex/releases/download/v2.6.4/flex-2.6.4.tar.lz
# md5 a04b480d7455f0f5bdc6d36959e08e4c
# dep dev/lang/m4 dev/lang/byacc dev/build/make stdenv

build() {
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
}
