# url https://ftp.gnu.org/gnu/grep/grep-3.6.tar.xz
# md5 f47fe27049510b2249dba7f862ac1b51
# dep boot/sed boot/make boot/coreutils boot/heirloom boot/bin/stdenv

build() {
    {% include 'build.sh' %}
}
