# url https://ftp.gnu.org/gnu/make/make-4.3.tar.gz
# md5 fc7a67ea86ace13195b0bce683fd4469
# dep boot/heirloom boot/bmake boot/bin/stdenv

build() {
    $untar $src/make-* && cd make-*

    export CPPFLAGS="-w -I./glob -Dglob=make_glob -Dglobfree=make_globfree -Dfnmatch=make_fnmatch $CPPFLAGS"
    export ACCEPT_INFERIOR_RM_PROGRAM=yes

    dash ./configure --prefix=$out --disable-load --disable-dependency-tracking
    bmake -j $make_thrs
    bmake install
}
