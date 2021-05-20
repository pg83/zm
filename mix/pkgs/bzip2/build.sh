$untar $src/bz* && cd bz*

make -j $make_thrs LDFLAGS="$LDFLAGS $LIBS" CFLAGS="$CPPFLAGS $CFLAGS" PREFIX="$out" install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lbz2 \$LDFLAGS"
EOF
