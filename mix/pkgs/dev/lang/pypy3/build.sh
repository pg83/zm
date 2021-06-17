$untar $src/pypy* && cd pypy*

cat << EOF > clang
#!$(which dash)
$(which clang) $CPPFLAGS $CFLAGS $LDFLAGS -w \$@
EOF

cat << EOF > clang++
#!$(which dash)
$(which clang++) $CPPFLAGS $CFLAGS $LDFLAGS -w \$@
EOF

chmod +x clang clang++

export TMPDIR=$(pwd)
export PATH="$(pwd):$PATH"
export CC=$(which clang)

/usr/bin/python2 rpython/bin/rpython --make-jobs $make_thrs -Ojit pypy/goal/targetpypystandalone.py
./pypy3-c lib_pypy/pypy_tools/build_cffi_imports.py

mkdir -p $out/{bin,include,lib,pypy3-c}
cp -R {include,lib_pypy,lib-python,pypy3-c} $out/pypy3-c
cp libpypy3-c.dylib $out/lib/
ln -s $out/pypy3-c/pypy3-c $out/bin/pypy3
