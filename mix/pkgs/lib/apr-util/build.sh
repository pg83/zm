$untar $src/apr* && cd apr*

dash ./configure $COFLAGS --prefix=$out --disable-shared --enable-static --with-dbm=gdbm --disable-util-dso
make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -laprutil-1 \$LDFLAGS"
export COFLAGS="--with-apr-util=$out --with-libapr-util=$out \$COFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
