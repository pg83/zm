$untar $src/v* && cd uchardet*

build_cmake_ninja -DBUILD_SHARED_LIBS=OFF ..

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -luchardet \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
export CMFLAGS="-DUCHARDET_LIBRARY=$out/lib/libuchardet.a -DUCHARDET_INCLUDE_DIR=$out/include/uchardet \$CMFLAGS"
EOF