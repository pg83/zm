# url https://ftp.gnu.org/pub/gnu/gettext/gettext-0.21.tar.gz
# md5 28b1cd4c94a74428723ed966c38cf479
# lib lib/iconv lib/unistring
# dep tool/compress/gzip tool/gnu/findutils boot/make stdenv/mini

build() {
    $untar $src/gettext* && cd gettext*

    ln -s $(which dash) sh
    export PATH="$(pwd):$PATH"
    export CPPFLAGS="-Dlocale_charset=intl_locale_charset $CPPFLAGS"

    dash ./configure $COFLAGS --prefix=$out --disable-shared --enable-static --with-included-libxml --with-included-gettext --enable-relocatable --disable-c++
    make -j $make_thrs
    make install

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-framework CoreFoundation -L$out/lib -lintl \$LDFLAGS"
export COFLAGS="--with-libintl-prefix=$out \$COFLAGS"
EOF
}
