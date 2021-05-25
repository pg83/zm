$untar $src/v* && cd ninja*

export CC=gcc
export CXX=g++

export CFLAGS="$CPPFLAGS $CFLAGS"
export CXXFLAGS="$CPPFLAGS $CXXFLAGS"
export LDFLAGS="$LDFLAGS $LIBS"

python3 ./configure.py --bootstrap
mkdir -p $out/bin && cp ninja $out/bin/
