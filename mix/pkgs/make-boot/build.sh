export CPPFLAGS="-I./glob -Dglob=make_glob -Dglobfree=make_globfree -DSTDC_HEADERS=1 -Dfnmatch=make_fnmatch -w $CPPFLAGS"
export CFLAGS="-isystem/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include $CFLAGS"
export LDFLAGS="-L/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/lib $LDFLAGS"
export GREP=grep
export EGREP=egrep
export ac_cv_type_pid_t=yes
export ac_cv_type_uid_t=yes

echo $SHELL

$exe $mix misc untar $src/make*
cd make-*
dash ./configure --prefix=$out --disable-load --disable-dependency-tracking
dash ./build.sh
mkdir $out/bin && cp make $out/bin/ && chmod +x $out/bin/make
