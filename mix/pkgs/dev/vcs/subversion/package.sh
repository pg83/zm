# url https://archive.apache.org/dist/subversion/subversion-1.14.1.tar.bz2
# md5 2eccc2c7451397e01a13682600af9563
# dep lib/z lib/lz4 lib/apr lib/intl lib/serf lib/expat lib/sqlite3
# dep lib/apr-util lib/utf8proc dev/build/make dev/build/pkg-config stdenv

build() {
    $untar $src/sub* && cd sub*

    export COFLAGS=$(echo "$COFLAGS" | tr ' ' '\n' | grep -v expat | tr '\n' ' ')
    export COFLAGS="$COFLAGS --with-expat=$lib_expat/include:$lib_expat/lib:-lexpat"

    dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
    make -j $make_thrs
    make install
}
