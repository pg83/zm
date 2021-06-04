$unzip $src/*.zip && cd awk*

make CC="gcc $CPPFLAGS $CFLAGS" HOSTCC="gcc $CPPFLAGS $CFLAGS"

mkdir $out/bin && cp a.out $out/bin/nawk
