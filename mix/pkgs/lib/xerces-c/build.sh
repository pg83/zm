$untar $src/xerces* && cd xerces*

build_cmake_ninja \
    -DBUILD_SHARED_LIBS=OFF \
    -Dnetwork-accessor=curl \
    -Dtranscoder=iconv \
    -Dmessage-loader=inmemory \
    -Dmutex-manager=standard \
    ..

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lxerces-c \$LDFLAGS"
export PKG_CONFIG_PATH="$out/lib/pkgconfig:\$PKG_CONFIG_PATH"
export CMFLAGS="-DXERCESC_INCLUDE_DIR=$out/include \$CMFLAGS"
EOF
