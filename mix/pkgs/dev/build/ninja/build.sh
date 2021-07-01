$untar $src/v* && cd ninja*

setup_compiler
python3 ./configure.py --bootstrap
mkdir -p $out/bin && cp ninja $out/bin/
