$untar $src/bash* && cd bash*

export CFLAGS="-fpermissive $CFLAGS -w"
export LIBS="$LDFLAGS $LIBS"
export CFLAGS="$CFLAGS $LIBS -Dsh_unset_nodelay_mode=bash_sh_unset_nodelay_mode -Dsh_get_env_value=bash_sh_get_env_value -Dsh_get_env_value=bash_sh_get_env_value -Dsh_get_home_dir=bash_sh_get_home_dir -Dsh_set_lines_and_columns=bash_sh_set_lines_and_columns -Dxfree=bash_xfree -Dsh_single_quote=bash_sh_single_quote -Dis_basic_table=bash_is_basic_table"

dash ./configure $COFLAGS \
     --prefix=$out \
     --without-bash-malloc \
     --disable-nls \
     --disable-extended-glob-default \
     --enable-extended-glob \
     --enable-job-control \
     --with-installed-readline \
     --enable-readline

make LIBS_FOR_BUILD="$LIBS" #-j $make_thrs
make install
