$unzip $src/664* && cd apple*

export INSTALLPREFIX=$out
export JOBS=$make_thrs

ln -s $(which dash) sh

cat << EOF > gcc
#!/bin/sh
$(which gcc) $CPPFLAGS $CFLAGS $LDFLAGS -w \$@
EOF

cat << EOF > g++
#!/bin/sh
$(which g++) $CPPFLAGS $CXXFLAGS $LDFLAGS -w \$@
EOF

ln -s gcc clang
ln -s g++ clang++

chmod +x gcc g++

export PATH="$(pwd):$PATH"

cat ./build.sh | grep -v 'CMAKE_EXTRA_ARGS=' > tmp_build.sh

export CMAKE_EXTRA_ARGS="-DLLVM_BUILD_LLVM_DYLIB=OFF"

/bin/bash ./tmp_build.sh
/bin/bash ./install.sh
