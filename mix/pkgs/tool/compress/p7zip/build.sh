$untar $src/p7zip* && cd p7zip*

export CFLAGS="-w -O2 $CPPFLAGS $CFLAGS"
export CXXFLAGS="-w -O2 $CPPFLAGS $CXXFLAGS -std=c++03"

make -j $make_thrs -f makefile \
     DEST_DIR=$out \
     CC=gcc \
     CXX=g++ \
     ALLFLAGS_C="$CFLAGS" \
     ALLFLAGS_CPP="$CXXFLAGS" \
     LDFLAGS="$LDFLAGS $LIBS" \
     7za install

(
    cd $out/usr/local/ && mv * $out/
    rm -rf $out/usr
)

mkdir $out/bin
install bin/7za $out/bin/
