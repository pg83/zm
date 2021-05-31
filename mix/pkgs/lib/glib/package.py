def package(mix):
    libs = [
        'lib/z',
        'lib/pcre',
        'lib/iconv',
        'lib/ffi',
        'lib/intl',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://download-fallback.gnome.org/sources/glib/2.68/glib-2.68.2.tar.xz',
                    'md5': '8d288416da38476c71998e5c2d3602ed',
                },
            ],
            'depends': libs + [
                'dev/build/meson',
                'dev/build/ninja',
                'boot/pkg-config',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
