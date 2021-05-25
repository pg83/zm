mkcd $out/bin/pkg
untar $src/dash-*
cd $out/bin
ln -s pkg/dash/*/bin/dash dash
