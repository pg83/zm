$untar $src/Python* && cd Python*

base64 -d << EOF > fix.py
{{mix.base64(mix.files.fix_py.data)}}
EOF

export MACOSX_DEPLOYMENT_TARGET=11.0
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

./python.exe ./fix.py patch ./setup.py
DUMP=1 ./python.exe ./setup.py build > data.json
./python.exe ./fix.py ./data.json > Modules/Setup.local

make -j $make_thrs
make install
