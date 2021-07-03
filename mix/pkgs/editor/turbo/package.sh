# url https://github.com/magiblot/turbo/archive/971aad35d4b705228caa8852114438ee71d488d8.zip
# md5 53d2cdb6a47cad1796d32dc5839726e8
# dep lib/cxx lib/fmt lib/tvision lib/clipboard dev/build/cmake stdenv

build() {
    $unzip $src/*.zip && cd turbo*

    echo 'install(TARGETS turbo DESTINATION bin)' >> CMakeLists.txt

    build_cmake_ninja \
        -DTURBO_USE_SYSTEM_DEPS=ON \
        -DTURBO_USE_SYSTEM_TVISION=ON \
        -DCMAKE_PREFIX_PATH="$lib_clipboard;$lib_tvision" \
        ..
}
