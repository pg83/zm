# url https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.16.tar.gz
# md5 7d2a800b952942bb2880efb00cfd524c
# build-depends boot/make boot/autohell boot/coreutils boot/bin/stdenv

build() {
    {% include 'build.sh' %}
}
