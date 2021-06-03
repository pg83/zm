$untar $src/unrar* && cd unrar*

make CXX=g++ CC=gcc LDFLAGS="$LDFLAGS" CPPFLAGS="" CXXFLAGS="-O2 $CPPFLAGS $CXXFLAGS" -j $make_thrs -f makefile
mkdir -p $out/bin
install -v -m755 unrar $out/bin/
