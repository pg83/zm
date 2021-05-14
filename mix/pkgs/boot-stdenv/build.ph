cd $out

---
data = '''
export CPPFLAGS="-isystem/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include"
export LDFLAGS="-L/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/lib"
'''

with open('env', 'w') as f:
    f.write(data)
---

mkcd $out/bin

ln -s $bin_darwin_clang/bin/clang gcc
ln -s $bin_darwin_clang/bin/clang++ g++
ln -s $bin_darwin_clang/bin/clang-cpp cpp

ln -s $bin_darwin_clang/bin/llvm-ar ar
ln -s $bin_darwin_clang/bin/llvm-ranlib ranlib
ln -s $bin_darwin_clang/bin/llvm-strip strip
ln -s $bin_darwin_clang/bin/llvm-nm nm

ln -s /usr/bin/ld ld
