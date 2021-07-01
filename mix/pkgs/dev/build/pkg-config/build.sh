$untar $src/pkg* && cd pkg*

ln -s $(which dash) sh

export PATH="$(pwd):$PATH"
export LDFLAGS="$LDFLAGS $LIBS"
export GLIB_LIBS="$LIBS"

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared --disable-host-tool
make -j $make_thrs
make install

cat << EOF > $out/env
export PKG_CONFIG="$out/bin/pkg-config"
EOF
