# url https://www.cpan.org/src/5.0/perl-5.34.0.tar.gz
# md5 2acf2ef147e41730e572251ed079bc1a
# dep lib/z lib/gdbm lib/iconv lib/compiler_rt dev/build/make tool/gnu/coreutils shell/bash env/compiler stdenv

build() {
    $untar $src/perl* && cd perl*

    echo > empty.c
    gcc -c empty.c -o empty.o
    ar q libdl.a empty.o

    ln -s $(which bash) sh

    export PATH="$(pwd):$PATH"
    export LDFLAGS="-L$(pwd) $LDFLAGS"

    setup_compiler

    bash ./Configure -des \
        -Dusethreads \
        -Duse64bitall \
        -Dprefix="$out" \
        -Duseperlio \
        -Uusesfio \
        -Duseshrplib=false \
        -Dusedl=false \
        -Dcc=gcc \
        -Duserelocatableinc

    make -j $make_thrs
    make install
}
