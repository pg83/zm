$untar $src/termcap* && cd termcap*

dash ./configure $COFLAGS --prefix=$out --disable-shared --enable-static
make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -ltermcap \$LDFLAGS"
EOF
