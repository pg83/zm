{% include '//util/fetch_llvm.sh' %}
# lib boot/libcxxrt
# dep boot/coreutils boot/bin/stdenv

build() {
    {% include 'build.sh' %}
}
