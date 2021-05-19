$untar $src/llvm* && cd llvm* &&

export CPPFLAGS="-w -DNDEBUG -U__SSE2__ -I$out/include/c++/v1 $CPPFLAGS"
ln -s $(which dash) sh
export PATH="$(pwd):$PATH"

build_cmake_make -DLIBUNWIND_ENABLE_SHARED=NO -DLIBUNWIND_ENABLE_STATIC=YES ../libunwind
export LIBS="$out/lib/libunwind.a $LIBS"

build_cmake_make -DLIBCXXABI_ENABLE_SHARED=NO -DLIBCXXABI_ENABLE_STATIC=YES ../libcxxabi
export LIBS="$out/lib/libc++abi.a $LIBS"

build_cmake_make -DLIBCXX_ENABLE_SHARED=NO -DLIBCXX_ENABLE_STATIC=YES -DLIBCXX_CXX_ABI=libcxxabi ../libcxx
export LIBS="$out/lib/libc++.a $LIBS"

build_cmake_make -DLLVM_BUILD_LLVM_DYLIB=OFF -DLLVM_ENABLE_PROJECTS="clang;lld;polly" ../llvm
