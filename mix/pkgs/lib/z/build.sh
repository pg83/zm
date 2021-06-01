$untar $src/zlib* && cd zlib*

export CFLAGS="$CPPFLAGS $CFLAGS"
export LDFLAGS="$LDFLAGS $LIBS"
export TEST_LDFLAGS="$LDFLAGS -L. libz.a"

dash ./configure $COFLAGS --static --64 --prefix=$out
make -j $make_thrs TEST_LDFLAGS="$TEST_LDFLAGS"
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lz \$LDFLAGS"
export COFLAGS="--with-z=$out \$COFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
export CMFLAGS="-DZLIB_LIBRARY=$out/lib/libz.a -DZLIB_INCLUDE_DIR=$out/include -DCMAKE_USE_SYSTEM_ZLIB=ON \$CMFLAGS"
EOF
