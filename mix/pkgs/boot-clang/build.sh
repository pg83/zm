$untar $src/llvm* && cd llvm*

export CPPFLAGS="-w -DNDEBUG -U__SSE2__ $CPPFLAGS"
ln -s $(which dash) sh
export PATH="$(pwd):$PATH"

build_cmake_ninja -DLLVM_ENABLE_PROJECTS="clang;lld;polly" -DLLVM_BUILD_LLVM_DYLIB=OFF ../llvm
