$untar $src/zstd* && cd zstd*

make PREFIX=$out CC=gcc CXX=g++ -j $make_thrs install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lzstd \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
