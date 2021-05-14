cd $out

echo '. $darwin_env/env' >> env
echo 'export GREP=grep' >> env

mkdir bin && cd bin

ln -s $bin_darwin_clang/bin/clang gcc
ln -s $bin_darwin_clang/bin/clang++ g++
ln -s $bin_darwin_clang/bin/clang-cpp cpp

ln -s $bin_darwin_clang/bin/llvm-ar ar
ln -s $bin_darwin_clang/bin/llvm-ranlib ranlib
ln -s $bin_darwin_clang/bin/llvm-strip strip
ln -s $bin_darwin_clang/bin/llvm-nm nm

ln -s /usr/bin/grep grep
ln -s /usr/bin/egrep egrep
ln -s /usr/bin/awk awk

ln -s /usr/bin/ld ld
