# build-fetch-url https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.1-rc3/compiler-rt-12.0.1rc3.src.tar.xz
# build-fetch-md5 5650195210d1fb4f13676fcee98af1f0
# build-depends boot/coreutils boot/bin/stdenv

build() {
    {% include 'build.sh' %}
}
