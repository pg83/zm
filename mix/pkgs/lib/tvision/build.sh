$unzip $src/*.zip && cd tvision*

export CXXFLAGS="$CPPFLAGS $CXXFLAGS $LDFLAGS"

build_cmake_ninja -DCMAKE_PREFIX_PATH=$lib_ncurses ..

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -ltvision \$LDFLAGS"
EOF
