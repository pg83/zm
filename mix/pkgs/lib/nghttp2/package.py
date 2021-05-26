def package(mix):
    libs = [
        'lib/z',
        'lib/c-ares',
        'lib/openssl',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/nghttp2/nghttp2/releases/download/v1.43.0/nghttp2-1.43.0.tar.xz',
                },
            ],
            'depends': libs + [
                'dev/build/pkg-config',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
