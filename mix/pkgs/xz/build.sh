$untar $src/xz* && cd xz*

dash ./configure $COFLAGS --prefix $out --enable-static --disable-shared
make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -llzma \$LDFLAGS"
export COFLAGS="--with-lzma=$out \$COFLAGS"
EOF
