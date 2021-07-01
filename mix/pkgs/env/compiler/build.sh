setup_compiler() {
cat << EOF > clang
#!$(which dash)
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
