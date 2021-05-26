$untar $src/v* && cd git*

ln -s $(which dash) sh
ln -s $(which bsdtar) tar
ln -s $(which bsdcpio) cpio

export PATH="$(pwd):$PATH"

(
dash ./configure $COFLAGS \
     --prefix=$out \
     --enable-static \
     --disable-shared \
     --with-python=$(which python3) \
     --with-perl=$(which perl) \
     --with-shell=$(which dash)
) || true

make prefix=$out V=1 CC=gcc LDFLAGS="$LDFLAGS" INSTALL_SYMLINKS=yes -j $make_thrs
make prefix=$out V=1 CC=gcc LDFLAGS="$LDFLAGS" INSTALL_SYMLINKS=yes install
