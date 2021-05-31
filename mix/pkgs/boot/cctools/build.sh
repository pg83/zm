$unzip $src/236* && cd cctools* && cd cctools

export CPPFLAGS="-D__crashreporter_info__=__crashreporter_info_ld__ $CPPFLAGS"

cat << EOF > fake.c
void __objc_personality_v0() {
}

void objc_terminate() {
}
EOF

gcc -c fake.c -o fake.o
ar q libfake.a fake.o

export LDFLAGS="-L$(pwd) -L$(pwd)/libobjc2/.libs -lfake $LDFLAGS"

dash ./configure $COFLAGS \
     --prefix=$out \
     --with-sysroot=$OSX_SDK \
     --enable-static \
     --disable-shared \
     --enable-tapi-support \
     --with-libtapi=$boot_cctools_libtapi

(
    cd libobjc2 && make -j $make_thrs
)

make -j $make_thrs || touch ld64/src/other/ObjectDump
make -j $make_thrs
make install
