# url https://github.com/tpoechtrager/cctools-port/archive/236a426c1205a3bfcf0dbb2e2faf2296f0a100e5.zip
# md5 3ba3b9f5e6ebc2afe77cdafeaaeeb981
# dep boot/libcxx boot/cctools/libtapi boot/autohell boot/diffutils boot/coreutils boot/bin/stdenv

build() {
    $unzip $src/*.zip && cd cctools* && cd cctools

    export CPPFLAGS="-D__crashreporter_info__=__crashreporter_info_ld__ $CPPFLAGS"
    export LDFLAGS="-L$(pwd)/libobjc2/.libs $LDFLAGS"

    dash ./configure $COFLAGS \
        --prefix=$out \
        --with-sysroot=$OSX_SDK \
        --enable-static \
        --disable-shared \
        --enable-tapi-support \
        --with-libtapi=$(dirname $(which tapi))

    (
        cd libobjc2
        sed -e 's/-fblocks/-fblocks -fno-objc-exceptions/' -i Makefile
        make -j $make_thrs
    )

    make -j $make_thrs || touch ld64/src/other/ObjectDump
    make -j $make_thrs
    make install
}
