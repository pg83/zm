def package(mix):
    libs = [
        'lib/z',
        'lib/idn2',
        'lib/openssl',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/curl/curl/releases/download/curl-7_76_1/curl-7.76.1.tar.xz',
                },
            ],
            'depends': libs + [
                'tool/build/pkg-config',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
