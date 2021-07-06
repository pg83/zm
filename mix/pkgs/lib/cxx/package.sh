# dep boot/ninja boot/cmake stdenv
{% include '//util/fetch_llvm.sh' %}

build() {
    $untar $src/llvm* && cd llvm*

    {% include '//util/build_libcxx.sh' %}

    cat << EOF > $out/env
export CPPFLAGS="-I$out/include/c++/v1 \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lunwind -lc++abi -lc++ \$LDFLAGS"
EOF
}
