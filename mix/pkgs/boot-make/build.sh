export CPPFLAGS="$CPPFLAGS -I./glob -Dglob=make_glob -Dglobfree=make_globfree -Dfnmatch=make_fnmatch -w"

$untar $src/make-* && cd make-*

dash ./configure --prefix=$out --disable-load --disable-dependency-tracking
dash ./build.sh
mkdir $out/bin && cp make $out/bin/ && chmod +x $out/bin/make
