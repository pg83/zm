# url https://ftp.gnu.org/gnu/coreutils/coreutils-8.32.tar.xz
# md5 022042695b7d5bcf1a93559a9735e668
# dep boot/make boot/which boot/heirloom boot/bin/stdenv env/compiler

build () {
    {% include 'build.sh' %}
}
