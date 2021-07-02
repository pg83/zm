# url https://github.com/ninja-build/ninja/archive/refs/tags/v1.10.2.tar.gz
# md5 639f75bc2e3b19ab893eaf2c810d4eb4
# dep boot/sed boot/which boot/python boot/libcxx boot/coreutils boot/bin/stdenv env/compiler

build() {
    {% include '//dev/build/ninja/build.sh' %}
}
