cd $out
untar $src/clang*
ln -s clang*/bin bin
unlink clang*/lib/*.a
unlink clang*/lib/*.dylib
