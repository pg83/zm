# url http://gondor.apana.org.au/~herbert/dash/files/dash-0.5.11.3.tar.gz
# md5 c7016b513f701d88c70b3082eb183581
# build-depends boot/which
# build-depends boot/autohell
# build-depends boot/coreutils
# build-depends boot/bin/stdenv
# build-depends env/compiler

build () {
    {% include 'build.sh' %}
}
