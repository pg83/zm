$untar $src/mpdecimal* && cd mpdecimal*

setup_compiler

dash ./configure $COFLAGS --prefix=$out --disable-shared --enable-static --enable-cxx=no
make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lmpdec \$LDFLAGS"
EOF
