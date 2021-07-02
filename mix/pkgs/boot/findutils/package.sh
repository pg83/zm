# url https://ftp.gnu.org/gnu/findutils/findutils-4.8.0.tar.xz
# md5 eeefe2e6380931a77dfa6d9350b43186
# dep boot/autohell boot/coreutils boot/bin/stdenv

build() {
    $untar $src/find* && cd find*

    (cd gl/lib/malloc && echo '#define __nonnull(x)' > tmp && cat dynarray-skeleton.c >> tmp && mv tmp dynarray-skeleton.c)

    dash ./configure $COFLAGS --prefix=$out --enable-static --disable-shared
    make -j $make_thrs
    make install
}
