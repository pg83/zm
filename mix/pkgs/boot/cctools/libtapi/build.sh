$unzip $src/*.zip && cd apple*

(
    cd src/llvm/projects/libtapi/tools/libtapi
    cat CMakeLists.txt | sed -e 's/SHARED/STATIC/' > tmp && mv tmp CMakeLists.txt
)

export CPPFLAGS="-I$(pwd)/src/llvm/projects/clang/include -I$(pwd)/build/projects/clang/include $CPPFLAGS"

ln -s $(which dash) sh

setup_compiler

build_cmake_prepare \
    -DLLVM_INCLUDE_TESTS=OFF \
    -DTAPI_REPOSITORY_STRING=1100.0.11 \
    -DTAPI_FULL_VERSION=11.0.0 \
    ../src/llvm

cd build && make -j $make_thrs

for p in projects/libtapi/tools/tapi projects/libtapi/tools/libtapi projects/libtapi/include; do
    (
        cd $p
        make -j $make_thrs install
    )
done

(
    cp lib/*.a $out/lib/
)

libtool -static -o libtapi.a $out/lib/*.a && rm $out/lib/*.a && mv libtapi.a $out/lib/

cat << EOF > $out/env
export LDFLAGS="-L$out/lib -ltapi \$LDFLAGS"
export CPPFLAGS="-I$out/include \$CPPFLAGS"
EOF
