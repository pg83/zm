def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://pkg-config.freedesktop.org/releases/pkg-config-0.29.2.tar.gz',
                },
            ],
            'depends': [
                'glib',
                'iconv',
                'stdenv',
                'boot-pkg-config',
            ],
        },
    }
