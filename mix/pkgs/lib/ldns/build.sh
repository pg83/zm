$untar $src/ldns* && cd ldns*

ln -s $(which dash) sh
export PATH="$(pwd):$PATH"

dash ./configure $COFLAGS \
     --prefix=$out \
     --enable-static \
     --disable-shared \
     --with-ssl=$lib_openssl \
     --with-drill

make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lldns \$LDFLAGS"
export COFLAGS="--with-ldns=$out \$COFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
