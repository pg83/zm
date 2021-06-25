$untar $src/coreutils-* && cd coreutils-*

export ACCEPT_INFERIOR_RM_PROGRAM=yes
export FORCE_UNSAFE_CONFIGURE=1
export CFLAGS="$CFLAGS $LDFLAGS $LIBS -w"

dash ./configure --prefix=$out --libexecdir=$out/bin --without-gmp --enable-no-install-program=stdbuf --enable-single-binary=symlinks

make LN_S=ln -j $make_thrs

export PATH="$(pwd)/src:$PATH"

make install
