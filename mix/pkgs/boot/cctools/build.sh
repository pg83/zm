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
