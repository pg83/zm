cd $out && mkdir bin && cd bin

clang_path=$(which clang)
clang_dir=$(dirname $clang_path)

ln -s $clang_dir/clang gcc
ln -s $clang_dir/clang++ g++
ln -s $clang_dir/clang-cpp cpp

ln -s $clang_dir/llvm-ar ar
ln -s $clang_dir/llvm-ranlib ranlib
ln -s $clang_dir/llvm-strip strip
ln -s $clang_dir/llvm-nm nm

ln -s /usr/bin/ld ld
