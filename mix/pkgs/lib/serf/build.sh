$untar $src/serf* && cd serf*

patch -p1 << EOF
{{mix.files.p00_patch.data}}
EOF

scons PREFIX=$out CFLAGS="$CPPFLAGS $CFLAGS" LINKFLAGS="$LDFLAGS $LIBS" OPENSSL="$lib_openssl" ZLIB="$lib_z" APR="$lib_apr" APU="$lib_apr_util"
scons install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lserf-1 \$LDFLAGS"
export COFLAGS="--with-serf=$out --with-libserf=$out \$COFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
