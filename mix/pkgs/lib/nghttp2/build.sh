$untar $src/nghttp2* && cd nghttp2*

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared --enable-lib-only
make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lnghttp2 \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
