# url https://github.com/Kitware/CMake/releases/download/v3.20.2/cmake-3.20.2.tar.gz
# md5 cd0e7735f1e51f30ee3b0844390a464a
# build-depends env/cmake boot/which boot/libcxx boot/autohell boot/coreutils boot/bin/stdenv env/compiler
# runtime-depends env/cmake

build () {
    {% include 'build.sh' %}
}
