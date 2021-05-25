$untar $src/lib* && cd lib*

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared --without-xml2 --without-expat
make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -larchive \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF