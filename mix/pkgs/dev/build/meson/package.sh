# url https://github.com/mesonbuild/meson/releases/download/0.58.0/meson-0.58.0.tar.gz
# md5 18ac55e3d6a5acb17b5737eb2a15bb5b
# dep stdenv/tiny stdenv/c
# run dev/lang/python3

build() {
    cd $out && $untar $src/meson* && ln -s meson* meson && mkdir bin && cd bin && ln -s ../meson/meson.py ./meson
}
