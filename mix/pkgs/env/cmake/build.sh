build_cmake_ps() {
    echo '' > ps && chmod +x ps
    export PATH="$(pwd):$PATH"
}

build_cmake_prepare() {
    export CPPFLAGS="-Wno-unused-command-line-argument $CPPFLAGS"
    export CXXFLAGS="-O2 $CPPFLAGS $CXXFLAGS"
    export CFLAGS="-O2 $CPPFLAGS $CFLAGS"

    (rm -rf build || true) && mkdir build && cd build

    build_cmake_ps

    cmake                                                                   \
        $CMFLAGS                                                            \
        -Wno-dev                                                            \
        -DCMAKE_INSTALL_PREFIX="$out"                                       \
        -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS $LIBS"                           \
        -DCMAKE_C_COMPILER="gcc"                                            \
        -DCMAKE_CXX_COMPILER="g++"                                          \
        -DCMAKE_BUILD_TYPE=Release                                          \
        -DCMAKE_C_FLAGS_RELEASE="$CFLAGS $LDFLAGS $LIBS"                    \
        -DCMAKE_CXX_FLAGS_RELEASE="$CXXFLAGS $LDFLAGS $LIBS"                \
        -DBUILD_SHARED_LIBS=OFF                                             \
        $@
}

build_cmake_make() {
    (
        build_cmake_prepare $@
        make VERBOSE=1 -j $make_thrs
        make install
    )
}

build_cmake_ninja() {
    (
        build_cmake_prepare -G Ninja $@
        ninja -j $make_thrs all
        ninja install
    )
}
