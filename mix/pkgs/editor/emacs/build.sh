$untar $src/emacs* && cd emacs*

(base64 -d | patch -p1) << EOF
{% include 'p00.diff#base64' %}
EOF

dash ./configure $COFLAGS \
     --prefix=$out \
     --enable-static \
     --disable-shared \
     --without-all \
     --without-x \
     --with-dumping=pdumper \
     --without-ns

make -j $make_thrs
make install
