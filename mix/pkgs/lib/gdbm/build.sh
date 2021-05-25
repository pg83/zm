$untar $src/gdbm* && cd gdbm*

dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared --enable-libgdbm-compat --with-readline
make -j $make_thrs
make install

cd $out/lib && ln -s libgdbm_compat.a libdbm.a

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lgdbm -lgdbm_compat \$LDFLAGS"
export COFLAGS="--with-gdbm=$out \$COFLAGS"
EOF
