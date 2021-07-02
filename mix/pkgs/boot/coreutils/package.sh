# url https://ftp.gnu.org/gnu/coreutils/coreutils-8.32.tar.xz
# md5 022042695b7d5bcf1a93559a9735e668
# build-depends boot/make
# build-depends boot/which
# build-depends boot/heirloom
# build-depends boot/bin/stdenv
# build-depends env/compiler

build () {
    {% include 'build.sh' %}
}
