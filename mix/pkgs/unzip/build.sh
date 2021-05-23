$untar $src/unzip* && cd unzip*

for i in `ls ../debian/patches/*.patch`; do
    cat "$i" | patch -p1
done

ln -s $(which dash) sh

cat << EOF > cc
gcc -w \$CFLAGS \$CPPFLAGS \$@
EOF

chmod +x cc

export PATH="$(pwd):$PATH"

make -f unix/Makefile macosx
make prefix=$out MANDIR=$out/share/man/man1 -f unix/Makefile install
