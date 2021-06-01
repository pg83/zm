export CPPFLAGS="-w -I./glob -Dglob=make_glob -Dglobfree=make_globfree -Dfnmatch=make_fnmatch $CPPFLAGS"

$untar $src/make-* && cd make-*

dash ./configure --prefix=$out --disable-load --disable-dependency-tracking

make -j $make_thrs
make install
