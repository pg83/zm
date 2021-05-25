$untar $src/sqlite* && cd sqlite*

export CFLAGS="-DSQLITE_OMIT_LOAD_EXTENSION=1 $CPPFLAGS $CFLAGS"
export CC="gcc $CPPFLAGS $CFLAGS"

dash ./configure $COFLAGS --disable-shared --enable-static --prefix=$out
make -j $make_thrs
make install

cat << EOF > $out/env
export SQLITE3_ROOT="$out"
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lsqlite3 \$LDFLAGS"
export COFLAGS="--with-sqlite3=$out \$COFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
