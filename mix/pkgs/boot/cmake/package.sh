# url https://github.com/Kitware/CMake/releases/download/v3.20.2/cmake-3.20.2.tar.gz
# md5 cd0e7735f1e51f30ee3b0844390a464a
# build-depends env/cmake
# build-depends boot/which
# build-depends boot/libcxx
# build-depends boot/autohell
# build-depends boot/coreutils
# build-depends boot/bin/stdenv
# build-depends env/compiler
# runtime-depends env/cmake

build () {
    {% include 'build.sh' %}
}
