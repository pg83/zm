$untar $src/v* && cd brotli*

make CC=gcc -j $make_thrs lib
cp -R ./c/include $out/
mkdir $out/lib && cp libbrotli.a $out/lib/

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lbrotli \$LDFLAGS"
EOF
