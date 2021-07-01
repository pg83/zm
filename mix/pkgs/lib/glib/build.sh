$untar $src/glib* && cd glib*

export CPPFLAGS=" -D_GNU_SOURCE=1 -I$(pwd)/inc $CPPFLAGS"

setup_compiler

echo 'int main() {}' > glib/tests/cxx.cpp
echo 'int main() {}' > tests/cxx-test.cpp

meson -Ddefault_library=static -Dprefix=$out _build && cd _build

ninja -j $make_thrs
ninja install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -framework CoreServices -framework Foundation -lglib-2.0 -lgobject-2.0 -lgio-2.0 -lgmodule-2.0 -lgthread-2.0 \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
