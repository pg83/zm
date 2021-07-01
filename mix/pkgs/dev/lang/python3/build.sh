$untar $src/Python* && cd Python*

base64 -d << EOF > fix.py
{% include 'fix.py/base64' %}
EOF

setup_compiler

export COFLAGS=$(echo "$COFLAGS" | tr ' ' '\n' | grep -v 'with-system-ffi' | tr '\n' ' ')

dash ./configure $COFLAGS \
     --prefix=$out \
     --enable-static \
     --disable-shared \
     --with-ensurepip=no \
     --with-system-libmpdec \
     --with-system-expat \
     --with-system-ffi

make -j $make_thrs

./python.exe ./fix.py patch ./setup.py
DUMP=1 ./python.exe ./setup.py build > data.json
./python.exe ./fix.py ./data.json > Modules/Setup.local

make -j $make_thrs
make install
