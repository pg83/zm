cat << EOF > which.c
{% include 'which.c' %}
EOF

mkdir $out/bin && gcc $CPPFLAGS $CFLAGS $LDFLAGS which.c -o $out/bin/which
