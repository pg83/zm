$untar $src/make-* && cd make-*

export CPPFLAGS="-w -I./glob -Dglob=make_glob -Dglobfree=make_globfree -Dfnmatch=make_fnmatch $CPPFLAGS"
export ACCEPT_INFERIOR_RM_PROGRAM=yes

dash ./configure --prefix=$out --disable-load --disable-dependency-tracking
dash ./build.sh && mv ./make ./newmake
./newmake clean
./newmake -j $make_thrs
./make install
