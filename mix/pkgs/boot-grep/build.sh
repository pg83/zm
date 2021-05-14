. $bin_stdenv/env

export GREP=
export EGREP=
export ac_cv_path_GREP=grep

$exe $mix misc untar $src/grep-* && cd grep-*

dash ./configure --prefix=$out
make
make install
