$untar $src/coreutils-* && cd coreutils-*

export FORCE_UNSAFE_CONFIGURE=1
export CFLAGS="$CFLAGS $LDFLAGS $LIBS -w"

dash ./configure --prefix=$out --libexecdir=$out/bin --without-gmp --enable-no-install-program=stdbuf --enable-single-binary=symlinks

make -j 8 || true

echo >> src/libstdbuf.c
echo >> 'int main() {}' >> src/libstdbuf.c

make -j 8
make install
