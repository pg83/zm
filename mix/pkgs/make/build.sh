. $boot_stdenv/env

export CPPFLAGS="$CPPFLAGS -I./glob -Dglob=make_glob -Dglobfree=make_globfree -Dfnmatch=make_fnmatch -w"

$exe $mix misc untar $src/make-* && cd make-*

dash ./configure --prefix=$out --disable-load --disable-dependency-tracking
make
make install
