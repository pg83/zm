$untar $src/expat* && cd expat*

dash ./configure $COFLAGS --prefix=$out --without-examples --enable-static --disable-shared
make -j $make_thrs
make install

cat << EOF > $out/env
export COFLAGS="--with-expat=$out \$COFLAGS"
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lexpat \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
export CMFLAGS="-DCMAKE_USE_SYSTEM_EXPAT=ON -DEXPAT_LIBRARY=$out/lib/libexpat.a -DEXPAT_INCLUDE_DIR=$out/include \$CMFLAGS"
EOF
