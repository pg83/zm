# url http://gondor.apana.org.au/~herbert/dash/files/dash-0.5.11.3.tar.gz
# md5 c7016b513f701d88c70b3082eb183581
# build-depends boot/which boot/autohell boot/coreutils boot/bin/stdenv env/compiler

build () {
    {% include 'build.sh' %}
}
