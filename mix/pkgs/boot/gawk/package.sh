# url https://mirror.tochlab.net/pub/gnu/gawk/gawk-5.1.0.tar.xz
# md5 8470c34eeecc41c1aa0c5d89e630df50
# dep boot/sed boot/grep boot/make boot/coreutils boot/heirloom boot/bin/stdenv

build() {
    {% include 'build.sh' %}
}
