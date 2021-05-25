$untar $src/readline* && cd readline*

export CFLAGS="-Dxmalloc=rl_xmalloc -Dxrealloc=Drl_xrealloc $CFLAGS"

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lreadline \$LDFLAGS"
export COFLAGS="--with-installed-readline=$out --with-readline=$out \$COFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
