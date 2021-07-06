# url https://ftp.gnu.org/gnu/bash/bash-5.1.tar.gz
# md5 bb91a17fd6c9032c26d0b2b78b50aff5
# dep lib/readline lib/ncurses lib/iconv lib/intl dev/build/make env/compiler stdenv

build() {
    $untar $src/bash* && cd bash*

    export CPPFLAGS="-fpermissive -w -Dsh_unset_nodelay_mode=bash_sh_unset_nodelay_mode -Dsh_get_env_value=bash_sh_get_env_value -Dsh_get_env_value=bash_sh_get_env_value -Dsh_get_home_dir=bash_sh_get_home_dir -Dsh_set_lines_and_columns=bash_sh_set_lines_and_columns -Dxfree=bash_xfree -Dsh_single_quote=bash_sh_single_quote -Dis_basic_table=bash_is_basic_table $CPPFLAGS"

    setup_compiler

    dash ./configure $COFLAGS \
        --prefix=$out \
        --without-bash-malloc \
        --disable-nls \
        --disable-extended-glob-default \
        --enable-extended-glob \
        --enable-job-control \
        --with-installed-readline \
        --enable-readline

    make
    make install
}
