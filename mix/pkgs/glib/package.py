def package(mix):
    libs = [
        'zlib',
        'pcre',
        'iconv',
        'libffi',
        'gettext',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://download-fallback.gnome.org/sources/glib/2.68/glib-2.68.2.tar.xz',
                },
            ],
            'depends': libs + [
                'stdenv',
                'meson',
                'ninja',
                'boot-pkg-config',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
