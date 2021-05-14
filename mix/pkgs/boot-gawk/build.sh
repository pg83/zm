. $bin_stdenv/env

$exe $mix misc untar $src/gawk-* && cd gawk-*

export CFLAGS="-Derr=gawk_err -Dxmalloc=gawk_xmalloc -Dxrealloc=Dgawk_xrealloc -Dregcomp=gawk_regcomp -Dregfree=gawk_regfree  $CFLAGS"

dash ./configure --prefix=$out --libexecdir=$out/bin/awk_exec --disable-shared --enable-static --disable-extensions
make
make install
