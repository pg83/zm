$untar $src/make-* && cd make-*

export CPPFLAGS="-I./glob -Dglob=make_glob -Dglobfree=make_globfree -Dfnmatch=make_fnmatch -w $CPPFLAGS"

dash ./configure $COFLAGS --prefix=$out --disable-load --disable-dependency-tracking
make -j $make_thrs
make install
