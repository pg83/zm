$untar $src/lib* && cd lib*

sed -e '/^includesdir/ s/$(libdir).*$/$(includedir)/' \
    -i include/Makefile.in

sed -e '/^includedir/ s/=.*$/=@includedir@/' \
    -e 's/^Cflags: -I${includedir}/Cflags:/' \
    -i libffi.pc.in

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
make -j $make_thrs
make install

cat << EOF > $out/env
export LIBFFI_CFLAGS="-I$out/include"
export LIBFFI_LIBS="-L$out/lib -lffi"
export CFLAGS="\$LIBFFI_CFLAGS \$CFLAGS"
export LDFLAGS="\$LIBFFI_LIBS \$LDFLAGS"
export COFLAGS="--with-system-ffi=$out \$COFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
