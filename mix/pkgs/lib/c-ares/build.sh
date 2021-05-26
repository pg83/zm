$untar $src/c* && cd c*

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared --disable-tests
make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lcares \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
