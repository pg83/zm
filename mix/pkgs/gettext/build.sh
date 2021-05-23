$untar $src/gettext* && cd gettext*

ln -s $(which dash) sh
export PATH="$(pwd):$PATH"

dash ./configure $COFLAGS --prefix=$out --disable-shared --enable-static --with-included-libxml --with-included-gettext --enable-relocatable --disable-c++
make -j $make_thrs
make install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-framework CoreFoundation -L$out/lib -lintl \$LDFLAGS"
export COFLAGS="--with-libintl-prefix=$out \$COFLAGS"
EOF
