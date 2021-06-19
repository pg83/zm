$unzip $src/*.zip && cd mrust*

setup_compiler

export shell=$(which bash)
export SHELL=$(which bash)

cat Makefile | sed -e 's/VERSION_GIT.*/QW -DVERSION_BUILDTIME=\\"\\" -DVERSION_GIT_ISDIRTY=1 -DVERSION_GIT_FULLHASH=\\"\\" -DVERSION_GIT_SHORTHASH=\\"\\" -DVERSION_GIT_BRANCH=1 /' | sed -e 's/-Wl,--whole-archive/-Wl,-all_load/' | sed -e 's/-Wl,--no-whole-archive/-Wl,-noall_load/' > qw && mv qw Makefile
bash -c "make CC=clang RUSTC_TARGET=x86_64-unknown-macosx -j $make_thrs -f minicargo.mk"
