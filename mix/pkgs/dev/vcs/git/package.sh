# url https://github.com/git/git/archive/refs/tags/v2.32.0-rc1.tar.gz
# md5 5977037fe36445a5b57872cb48335004
# dep lib/z lib/curl lib/iconv lib/expat lib/pcre2 lib/openssl dev/build/make dev/lang/perl5 dev/lang/python3 stdenv

build() {
    $untar $src/v* && cd git*

    ln -s $(which dash) sh
    ln -s $(which bsdtar) tar
    ln -s $(which bsdcpio) cpio

    export PATH="$(pwd):$PATH"

    make prefix=$out V=1 CC=gcc LDFLAGS="$LDFLAGS" INSTALL_SYMLINKS=yes -j $make_thrs install
}
