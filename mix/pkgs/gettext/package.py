def package(mix):
    libs = [
        'iconv',
        'libunistring',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/pub/gnu/gettext/gettext-0.21.tar.gz',
                },
            ],
            'depends': libs + [
                'gzip',
                'clang',
                'findutils',
                'boot-stdenv',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
