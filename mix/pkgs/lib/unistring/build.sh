$untar $src/lib* && cd lib*

ln -s $(which dash) sh
export PATH="$(pwd):$PATH"

dash ./configure $COFLAGS --prefix=$out --disable-shared --enable-static
make -j $make_thrs
make install

cat << EOF > $out/env
export COFLAGS="--with-libunistring-prefix=$out \$COFLAGS"
export LDFLAGS="-L$out/lib -lunistring \$LDFLAGS"
export CPPFLAGS="-I$out/include \$CPPFLAGS"
EOF
