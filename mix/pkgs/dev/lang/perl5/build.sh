$untar $src/perl* && cd perl*

echo > empty.c
gcc -c empty.c -o empty.o
ar q libdl.a empty.o

ln -s $(which bash) sh

export PATH="$(pwd):$PATH"
export LDFLAGS="-L$(pwd) $LDFLAGS"
export CFLAGS="-w $CPPFLAGS $CFLAGS"
export CXXFLAGS="$CFLAGS $CXXFLAGS"

bash ./Configure -des \
     -Accflags="$CFLAGS" \
     -Aldflags="$LDFLAGS $LIBS" \
     -Dusethreads \
     -Duse64bitall \
     -Dprefix=$out \
     -Duseperlio \
     -Uusesfio \
     -Duseshrplib=false \
     -Dusedl=false \
     -Dcc="gcc -Duserelocatableinc $CFLAGS $LDFLAGS $LIBS"

make -j $make_thrs
make install
