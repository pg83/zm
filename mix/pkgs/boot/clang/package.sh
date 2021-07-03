# url https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.0/llvm-project-12.0.0.src.tar.xz
# md5 5a4fab4d7fc84aefffb118ac2c8a4fc0
# dep boot/which boot/cmake boot/ninja boot/python boot/libcxx boot/autohell boot/coreutils boot/bin/stdenv
# run boot/cctools env/system

build() {
    $untar $src/llvm* && cd llvm*

    export CPPFLAGS="-DNDEBUG -U__SSE2__ $CPPFLAGS"
    ln -s $(which dash) sh
    export PATH="$(pwd):$PATH"

    build_cmake_ninja -DLLVM_ENABLE_PROJECTS="clang;lld;polly" -DLLVM_BUILD_LLVM_DYLIB=OFF ../llvm
}
