$unzip $src/664* && cd apple*

(
    cd src/llvm/projects/libtapi/tools/libtapi
    cat CMakeLists.txt | sed -e 's/SHARED/STATIC/' > tmp && mv tmp CMakeLists.txt
)

echo > ps && chmod +x ps
ln -s $(which dash) sh
setup_compiler
mkdir build && cd build

cmake ../src/llvm \
      -DCMAKE_CXX_FLAGS="-I$(pwd)/../src/llvm/projects/clang/include -I$(pwd)/projects/clang/include" \
      -DLLVM_INCLUDE_TESTS=OFF \
      -DCMAKE_BUILD_TYPE=RELEASE \
      -DCMAKE_INSTALL_PREFIX=$out \
      -DTAPI_REPOSITORY_STRING=1100.0.11 \
      -DTAPI_FULL_VERSION=11.0.0

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
