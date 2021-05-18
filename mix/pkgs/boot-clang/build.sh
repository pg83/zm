$untar $src/llvm* && cd llvm* && mkdir build && cd build

export CXXFLAGS="-O2 -DNDEBUG -w -U__SSE2__ $CPPFLAGS $CXXFLAGS"
export CFLAGS="-O2 -DNDEBUG -w -U__SSE2__ $CPPFLAGS $CFLAGS"

ln -s $(which dash) sh
export PATH="$(pwd):$PATH"

cmake -DCMAKE_INSTALL_PREFIX="$out"                                     \
      -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS $LIBS"                         \
      -DCMAKE_C_COMPILER="gcc"                                          \
      -DCMAKE_CXX_COMPILER="g++"                                        \
      -DCMAKE_BUILD_TYPE=Release                                        \
      -DCMAKE_C_FLAGS_RELEASE="$CFLAGS $LDFLAGS $LIBS"                  \
      -DCMAKE_CXX_FLAGS_RELEASE="$CXXFLAGS $LDFLAGS $LIBS"              \
      -DLLVM_ENABLE_PROJECTS="clang;lld;polly"                          \
      -DBUILD_SHARED_LIBS=OFF                                           \
      -DLLVM_BUILD_LLVM_DYLIB=OFF                                       \
      ../llvm

make VERBOSE=1 -j 8
make install
