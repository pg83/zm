# url https://github.com/libcxxrt/libcxxrt/archive/refs/heads/master.zip
# md5 3b43179e518dd0a54362267b255b9d24
# lib boot/libunwind
# dep boot/coreutils boot/bin/stdenv

build() {
    {% include 'build.sh' %}
}
