$untar $src/curl* && cd curl*


export LIBS=$(echo "$LDFLAGS" | tr ' ' '\n' | grep '^-l' | tr '\n' ' ')

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lcurl \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
export CMFLAGS="-DCURL_LIBRARY=$out/lib/libcurl.a -DCURL_INCLUDE_DIR=$out/include \$CMFLAGS"
EOF
