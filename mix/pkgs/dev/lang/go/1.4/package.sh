# url https://golang.org/dl/go1.4-bootstrap-20170531.tar.gz
# md5 d2cc61cb9f829b3510ee39c0c5568014
# dep shell/bash env/compiler stdenv

setup_compiler() {
cat << EOF > clang
#!$(which dash)
echo "\$@"
$(which clang) $CPPFLAGS $CFLAGS $LDFLAGS -w "\$@"
EOF

cat << EOF > clang++
#!$(which dash)
$(which clang++) $CPPFLAGS $CFLAGS $LDFLAGS -w "\$@"
EOF

chmod +x clang clang++

ln -s clang gcc
ln -s clang++ g++

export PATH="$(pwd):$PATH"
export CC=$(which clang)
export CXX=$(which clang++)
}

build() {
    cd $out && $untar $src/go* && cd go*

    setup_compiler

    (
        export GOROOT_FINAL="$out/go"
        cd src && cat run.bash | grep -v 'time go test' > qw && mv qw run.bash && bash ./all.bash
    )

    cd $out && ln -s go/bin ./

    cat << EOF > $out/env
export GOROOT_BOOTSTRAP="$out/go"
EOF
}
