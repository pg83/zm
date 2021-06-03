cd $out && mkdir bin && cd bin && $untar $src/SCons* && ln -s SCons* sconsdir

cat << EOF > scons
#!$(which dash)
PYTHONPATH=$(pwd)/sconsdir python3 $(pwd)/sconsdir/SCons/__main__.py "\$@"
EOF

chmod +x scons
