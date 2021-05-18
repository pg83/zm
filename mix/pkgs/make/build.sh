$untar $src/make-* && cd make-*

export CPPFLAGS="$CPPFLAGS -I./glob -Dglob=make_glob -Dglobfree=make_globfree -Dfnmatch=make_fnmatch -w"

dash ./configure --prefix=$out --disable-load --disable-dependency-tracking
make -j 8
make install
