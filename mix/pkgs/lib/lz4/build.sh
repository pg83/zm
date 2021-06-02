$untar $src/v* && cd lz4*

make PREFIX=$out CC=gcc CXX=g++ -j $make_thrs install

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -llz4 \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
EOF
