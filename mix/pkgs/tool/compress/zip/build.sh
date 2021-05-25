$untar $src/zip* && cd zip*

make -j $make_thrs -f unix/Makefile CC="gcc" CPP="gcc -E" CFLAGS="-I. $CPPFLAGS $CFLAGS -DUNIX" LFLAGS1="$LDFLAGS" zips
make -f unix/Makefile BINDIR="$out/bin" MANDIR="$out/man" install
