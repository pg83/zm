$untar $src/libedit* && cd libedit*

ln -s $(which dash) sh

export PATH="$(pwd):$PATH"
export CFLAGS="-D__STDC_ISO_10646__=1 $CFLAGS"

dash ./configure $COFLAGS --prefix=$out --disable-shared --enable-static
make -j $make_thrs
make install

cat << EOF > $out/env
export COFLAGS="--with-libedit=$out \$COFLAGS"
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -ledit \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
