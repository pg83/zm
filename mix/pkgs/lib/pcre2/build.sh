$untar $src/pcre* && cd pcre*

dash ./configure $COFLAGS --prefix=$out --disable-shared --enable-static --enable-pcre2grep-libz --enable-pcre2grep-libbz2 --enable-newline-is-anycrlf --enable-utf8 --enable-jit --enable-c++
make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lpcre2-8 \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
