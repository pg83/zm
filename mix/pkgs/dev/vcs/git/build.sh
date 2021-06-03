$untar $src/v* && cd git*

ln -s $(which dash) sh
ln -s $(which bsdtar) tar
ln -s $(which bsdcpio) cpio

export PATH="$(pwd):$PATH"

make prefix=$out V=1 CC=gcc LDFLAGS="$LDFLAGS" INSTALL_SYMLINKS=yes -j $make_thrs install
