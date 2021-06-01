def package(mix):
    libs = [
        'lib/iconv',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/libunistring/libunistring-0.9.10.tar.xz',
                    'md5': 'db08bb384e81968957f997ec9808926e',
                },
            ],
            'depends': libs + [
                'boot/make',
                'stdenv/mini',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
