$untar $src/slang* && cd slang*

export AR_CR="ar cr"
export CFLAGS="$CPPFLAGS $CFLAGS"

dash ./configure $COFLAGS \
     --disable-shared \
     --enable-static \
     --prefix=$out \
     --with-readline=gnu \
     --without-png \
     --without-onig

make AR_CR="$AR_CR" CFLAGS="$CFLAGS" install-static

cat << EOF > $out/env
export SLANG_CFLAGS="-I$out/include"
export SLANG_LIBS="-L$out/lib -lslang"
export CPPFLAGS="\$SLANG_CFLAGS \$CPPFLAGS"
export LDFLAGS="\$SLANG_LIBS \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
