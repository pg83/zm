{% include '//util/fetch_llvm.sh' %}
# dep boot/ninja boot/cmake boot/stdenv
# run dev/lang/cctools env/system

build() {
    $untar $src/llvm* && cd llvm*

    {% include '//util/build_libcxx.sh' %}

    build_cmake_ninja \
        -DLLVM_BUILD_LLVM_DYLIB=OFF \
        -DLLVM_LINK_LLVM_DYLIB=OFF \
        -DLLVM_ENABLE_PROJECTS="clang;lld;polly" \
        -DCLANG_LINK_CLANG_DYLIB=OFF \
        -DLLVM_POLLY_LINK_INTO_TOOLS=ON \
        -DLLVM_ENABLE_PIC=OFF \
        -DLLVM_DYLIB_COMPONENTS='' \
        -DBUILD_SHARED_LIBS=OFF \
        ../llvm
}
