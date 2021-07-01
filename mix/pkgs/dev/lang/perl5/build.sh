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
