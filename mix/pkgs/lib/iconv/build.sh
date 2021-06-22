$untar $src/libiconv* && cd libiconv*

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
make -j $make_thrs
make install

rm $out/lib/libcharset.a

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -liconv \$LDFLAGS"
export COFLAGS="--with-libiconv-prefix=$out --with-iconv=$out \$COFLAGS"
EOF
