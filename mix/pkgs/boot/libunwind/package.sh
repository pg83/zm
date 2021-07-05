{% include '//util/fetch_llvm.sh' %}
# dep boot/coreutils boot/bin/stdenv

build() {
    {% include 'build.sh' %}
}
