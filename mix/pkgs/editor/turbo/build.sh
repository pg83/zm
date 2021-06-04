$unzip $src/*.zip && cd turbo*

export CXXFLAGS="$CPPFLAGS $CXXFLAGS $LDFLAGS"

cat CMakeLists.txt
echo 'install(TARGETS turbo DESTINATION bin)' >> CMakeLists.txt

build_cmake_ninja \
    -DTURBO_USE_SYSTEM_DEPS=ON \
    -DTURBO_USE_SYSTEM_TVISION=ON \
    -DCMAKE_PREFIX_PATH="$lib_clipboard;$lib_tvision" \
    ..
