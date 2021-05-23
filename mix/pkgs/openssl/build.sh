$untar $src/openssl* && cd openssl*

export CC=gcc
export RANLIB=ranlib

perl ./Configure \
     darwin64-x86_64-cc \
     no-asm \
     threads \
     no-shared \
     no-dso \
     no-hw \
     no-tests \
     no-engine \
     --prefix=$out \
     --openssldir=$out \
     -w -std=c99 -D_GNU_SOURCE=1 $CFLAGS $LDFLAGS $LIBS

make -j $make_thrs
make install

cat << EOF > $out/env
export COFLAGS="--with-openssl=$out --with-openssldir=$out --with-ssl-dir=$out \$COFLAGS"
export OPENSSL_INCLUDES="-I$out/include"
export OPENSSL_LIBS="-L$out/lib -lssl"
export CPPFLAGS="\$OPENSSL_INCLUDES \$CPPFLAGS"
export LDFLAGS="\$OPENSSL_LIBS \$LDFLAGS"
EOF
