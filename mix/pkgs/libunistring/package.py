def package(mix):
    libs = [
        'iconv',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/libunistring/libunistring-0.9.10.tar.xz',
                },
            ],
            'depends': libs + [
                'clang',
                'boot-stdenv',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
