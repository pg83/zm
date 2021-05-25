$untar $src/Python* && cd Python*

export MACOSX_DEPLOYMENT_TARGET=11.0
export CFLAGS="$CPPFLAGS $CFLAGS"
export CXXFLAGS="$CPPFLAGS $CXXFLAGS"
export FCOFLAGS=$(echo "$COFLAGS" | tr ' ' '\n' | grep -v 'with-system-ffi' | tr '\n' ' ')
export COFLAGS="--with-system-ffi $FCOFLAGS"

dash ./configure $COFLAGS \
     --prefix=$out \
     --enable-static \
     --disable-shared \
     --with-ensurepip=no \
     --with-system-libmpdec \
     --with-system-expat

make -j $make_thrs
make install
