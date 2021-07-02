# url https://ftp.gnu.org/gnu/make/make-4.3.tar.gz
# md5 fc7a67ea86ace13195b0bce683fd4469
# dep boot/heirloom boot/bmake boot/bin/stdenv

build() {
    {% include 'build.sh' %}
}
