# url https://github.com/tpoechtrager/apple-libtapi/archive/664b8414f89612f2dfd35a9b679c345aa5389026.zip
# md5 30c0321c2099e3eac31110e5aaf56fbe
# dep boot/ninja boot/cmake boot/which boot/python boot/libcxx boot/autohell
# dep boot/diffutils boot/coreutils boot/bin/stdenv env/compiler env/cmake

build() {
    {% include 'build.sh' %}
}
