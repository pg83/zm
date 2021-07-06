# url https://github.com/magiblot/tvision/archive/c36e190174463ece471bdd1c06959fb8dc343c3c.zip
# md5 9c20bbe1511fe6d8b470f528467e2f27
# lib lib/cxx lib/ncurses
# dep dev/build/cmake stdenv

build() {
    $unzip $src/*.zip && cd tvision*

    export CXXFLAGS="$CPPFLAGS $CXXFLAGS $LDFLAGS"

    build_cmake_ninja -DCMAKE_PREFIX_PATH=$lib_ncurses ..

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -ltvision \$LDFLAGS"
EOF
}
