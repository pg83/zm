$untar $src/open* && cd open*

export CPPFLAGS="-D__APPLE_SANDBOX_NAMED_EXTERNAL__ $CPPFLAGS"
ln -s $lib_ncurses/lib/libncurses.a libcurses.a
export LDFLAGS="-L$(pwd) $LDFLAGS"

cat $src/*.diff | patch -p1

dash ./configure $COFLAGS --prefix=$out
make -j $make_thrs
make install
