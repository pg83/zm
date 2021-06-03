$untar $src/apr* && cd apr*

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared --disable-dso
make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lapr-1 \$LDFLAGS"
export COFLAGS="--with-apr=$out --with-libapr=$out \$COFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
