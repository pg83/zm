$untar $src/pypy* && cd pypy* && $untar $src/pyc*

export PYTHONPATH=$(echo $(pwd)/pyc*)

setup_compiler

python2 rpython/bin/rpython --make-jobs $make_thrs -Ojit pypy/goal/targetpypystandalone.py \
    --withoutmod-pyexpat \
    --withoutmod-zlib

./pypy3-c lib_pypy/pypy_tools/build_cffi_imports.py || true

for i in bin include lib pypy3-c; do
    mkdir -p $out/$i
done

for i in include lib_pypy lib-python pypy3-c; do
    cp -R $i $out/pypy3-c/
done

cp libpypy3-c.dylib $out/lib/
install_name_tool -change @rpath/libpypy3-c.dylib $out/lib/libpypy3-c.dylib $out/pypy3-c/pypy3-c
cd $out/bin &&  ln -s ../pypy3-c/pypy3-c pypy3

rm -rf $tmp

exit 0
