# url https://ftp.gnu.org/gnu/make/make-4.3.tar.gz
# md5 fc7a67ea86ace13195b0bce683fd4469
# dep lib/intl lib/iconv boot/make stdenv/mini

build() {
    $untar $src/make-* && cd make-*

    export CPPFLAGS="-I./glob -Dglob=make_glob -Dglobfree=make_globfree -Dfnmatch=make_fnmatch -w $CPPFLAGS"

    dash ./configure $COFLAGS --prefix=$out --disable-load --disable-dependency-tracking
    make -j $make_thrs
    make install
}
