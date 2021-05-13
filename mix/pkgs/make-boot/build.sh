export CPPFLAGS="-I./glob -Dglob=make_glob -Dglobfree=make_globfree -Dfnmatch=make_fnmatch -w $CPPFLAGS"

tar -xf $src/make*
cd make-*
./configure --prefix=$out --disable-load
./build.sh
mkdir $out/bin && cp make $out/bin/ && chmod +x $out/bin/make
