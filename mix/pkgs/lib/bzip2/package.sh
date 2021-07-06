# url https://www.sourceware.org/pub/bzip2/bzip2-latest.tar.gz
# md5 67e051268d0c475ea773822f7500d0e5
# dep dev/build/make stdenv/tiny stdenv/c

build() {
    $untar $src/bz* && cd bz*

    make -j $make_thrs LDFLAGS="$LDFLAGS $LIBS" CFLAGS="$CPPFLAGS $CFLAGS" PREFIX="$out" install

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lbz2 \$LDFLAGS"
EOF
}
