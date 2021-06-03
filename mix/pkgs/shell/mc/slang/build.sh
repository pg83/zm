$untar $src/mc* && cd mc*

cat << EOF > gcc
#!$(which dash)
$(which gcc) -w $CPPFLAGS $CFLAGS \$@
EOF

chmod +x gcc

export PATH="$(pwd):$PATH"

dash ./configure $COFLAGS \
     --prefix=$out \
     --disable-shared \
     --enable-static \
     --with-screen=slang \
     --with-search-engine=pcre

make -j $make_thrs
make install
