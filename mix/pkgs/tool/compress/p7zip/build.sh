$untar $src/p7zip* && cd p7zip*

cat makefile.linux_amd64 | grep -v 'PRE_COMP' | sed -e 's/CXX=.*/CXX=clang++/' | sed -e 's/CC=.*/CC=clang/' > makefile.machine
export CFLAGS="-w $CFLAGS"

make -f makefile \
     DEST_DIR=$out \
     CC=gcc \
     CXX=g++ \
     ALLFLAGS_C="$CFLAGS" \
     ALLFLAGS_CPP="$CXXFLAGS -std=c++03" \
     LDFLAGS="$LDFLAGS $LIBS" \
     7za install

(
    cd $out/usr/local/ && mv * $out/
    rm -rf $out/usr
)

mkdir $out/bin
install bin/7za $out/bin
