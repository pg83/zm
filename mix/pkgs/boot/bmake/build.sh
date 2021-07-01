cd $out && $untar $src/bmake* && cd bmake

(while read l; do printf "$l\n"; done) << EOF > config.h
{% include 'config.h' %}
EOF

gcc $CPPFLAGS $CFLAGS $LDFLAGS -w -I. \
    -DHAVE_CONFIG_H -DMAKE_NATIVE -DUSE_META -DBMAKE_PATH_MAX=1024 -D_PATH_DEFSYSPATH=\"$PWD/mk\" \
    arch.c buf.c compat.c cond.c dir.c enum.c for.c getopt.c \
    hash.c job.c lst.c main.c make.c make_malloc.c meta.c metachar.c \
    parse.c sigcompat.c str.c stresep.c suff.c targ.c trace.c util.c var.c -o bmake
