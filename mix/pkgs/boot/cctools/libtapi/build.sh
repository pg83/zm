$unzip $src/664* && cd apple*

(
    cd src/llvm/projects/libtapi/tools/libtapi
    cat CMakeLists.txt | sed -e 's/SHARED/STATIC/' > tmp && mv tmp CMakeLists.txt
)

mkdir build && cd build

dash=$(which dash)

ln -s $dash sh

cat << EOF > gcc
#!$dash
$(which gcc) $CPPFLAGS $CFLAGS $LDFLAGS -w \$@
EOF

cat << EOF > g++
#!$dash
$(which g++) $CPPFLAGS $CXXFLAGS $LDFLAGS -w \$@
EOF

ln -s gcc clang && ln -s g++ clang++ && chmod +x gcc g++

export PATH="$(pwd):$PATH"

cmake ../src/llvm \
      -DCMAKE_CXX_FLAGS="-I$(pwd)/../src/llvm/projects/clang/include -I$(pwd)/projects/clang/include" \
      -DLLVM_INCLUDE_TESTS=OFF \
      -DCMAKE_BUILD_TYPE=RELEASE \
      -DCMAKE_INSTALL_PREFIX=$out \
      -DTAPI_REPOSITORY_STRING=1100.0.11 \
      -DTAPI_FULL_VERSION=11.0.0

(
    cd projects/libtapi/tools/tapi
    make -j $make_thrs install
)

(
    cd projects/libtapi/tools/libtapi
    make -j $make_thrs install
)

(
    cd projects/libtapi/include
    make -j $make_thrs install
)

(
    cp lib/*.a $out/lib/
)

export LDFLAGS1=`(cd $out/lib && echo lib*.a) | sort | tr ' ' '\n' | sed -e 's/lib/-l/' | sed -e 's/\.a//' | tr '\n' ' '`

cat << EOF > $out/env
export LDFLAGS="-L$out/lib $LDFLAGS1 \$LDFLAGS"
export CPPFLAGS="-I$out/include \$CPPFLAGS"
EOF
