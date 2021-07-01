$untar $src/Python* && cd Python*

export CFLAGS="$CPPFLAGS $CFLAGS"
export CXXFLAGS="$CPPFLAGS $CXXFLAGS"
export FCOFLAGS=$(echo "$COFLAGS" | tr ' ' '\n' | grep -v 'with-system-ffi' | tr '\n' ' ')
export COFLAGS="--with-system-ffi $FCOFLAGS"

dash ./configure $COFLAGS \
     --prefix=$out \
     --enable-static \
     --disable-shared \
     --with-ensurepip=no \
     --with-system-libmpdec \
     --with-system-expat

make -j $make_thrs
make install

cat << EOF >> $out/lib/python2.7/ctypes/macholib/dyld.py
old_dyld_find = dyld_find

def dyld_find(name, executable_path=None, env=None):
    if name == 'libc.dylib':
        return '/usr/lib/libc.dylib'

    return old_dyld_find(name, executable_path, env)
EOF
