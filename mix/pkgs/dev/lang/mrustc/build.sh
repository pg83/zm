$unzip $src/*.zip && cd mrust* && ln -s $src/rustc* ./

echo > empty.c
gcc -c empty.c -o empty.o
ar q librt.a empty.o
cp librt.a libstdc++.a
cp librt.a libgcc_s.a
cp librt.a libSecurity.a
cp librt.a libCoreFoundation.a

cat << EOF > fake.c
int CFMutableAttributedStringGetTypeID() {return 0;}
void ENGINE_load_builtin_engines() {}
void ENGINE_register_all_complete() {}
EOF

gcc -c fake.c -o fake.o
ar q libfakefake.a fake.o

export LDFLAGS="-L$(pwd) -framework CoreFoundation -framework Security -lfakefake -lresolv $LDFLAGS"

setup_compiler

echo > ps && chmod +x ps
ln -s $(which bash) sh
ln -s gcc cc

(cd script-overrides && ln -s stable-1.29.0-linux stable-1.29.0-macos)
(cd script-overrides && ln -s stable-1.39.0-linux stable-1.39.0-macos)

cat Makefile | sed -e 's/VERSION_GIT.*/QW -DVERSION_BUILDTIME=\\"\\" -DVERSION_GIT_ISDIRTY=1 -DVERSION_GIT_FULLHASH=\\"\\" -DVERSION_GIT_SHORTHASH=\\"\\" -DVERSION_GIT_BRANCH=1 /' | sed -e 's/-Wl,--whole-archive/-Wl,-all_load/' | sed -e 's/-Wl,--no-whole-archive/-Wl,-noall_load/' > qw && mv qw Makefile
cat Makefile | sed -e 's/rcD/rc/' > qw && mv qw Makefile
cat src/trans/codegen_c.cpp | sed -e 's/asm(/asm(\\"_\\"/' > qw && mv qw src/trans/codegen_c.cpp
cat tools/minicargo/manifest.cpp | grep -v 'TODO: rustc-link-lib' > qw && mv qw tools/minicargo/manifest.cpp

unset OPENSSL_LIBS
unset OPENSSL_INCLUDE
unset OPENSSL_INCLUDES

export ZLIB_LIBRARY="$lib_z/lib/libz.a"
export ZLIB_INCLUDE_DIR="$lib_z/include"
export DEP_Z_INCLUDE="$lib_z/include"
export DEP_Z_ROOT="$lib_z"
export DEP_OPENSSL_ROOT="$lib_openssl"
export DEP_OPENSSL_INCLUDE="$lib_openssl/include"

bash << EOF
set -e
set -x

make RUSTCSRC
make V= CC=$(which clang) RUSTC_TARGET=x86_64-apple-darwin -j $make_thrs -f minicargo.mk || true
make V= CC=$(which clang) RUSTC_TARGET=x86_64-apple-darwin -j $make_thrs -f minicargo.mk
make V= CC=$(which clang) RUSTC_TARGET=x86_64-apple-darwin -C run_rustc

exit 1
EOF
