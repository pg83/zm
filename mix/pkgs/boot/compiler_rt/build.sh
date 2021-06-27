$untar $src/c* && cd c*

for x in lib/builtins/*.c; do
    clang $CPPFLAGS $CFLAGS -w -c $x
done

ar q libcompiler_rt.a *.o
ranlib libcompiler_rt.a

mkdir $out/lib && cp libcompiler_rt.a $out/lib/

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LDFLAGS="-L$out/lib -lcompiler_rt \$LDFLAGS"
EOF
