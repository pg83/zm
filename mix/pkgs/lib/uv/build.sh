$untar $src/libuv* && cd libuv*

export LIBTOOLIZE=libtoolize

dash ./autogen.sh
dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -luv \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
export CMFLAGS="-DCMAKE_USE_SYSTEM_LIBUV=ON -DLibUV_LIBRARY=$out/lib/libuv.a -DLibUV_INCLUDE_DIR=$out/include \$CMFLAGS"
EOF