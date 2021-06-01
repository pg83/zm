def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://c-ares.haxx.se/download/c-ares-1.17.1.tar.gz',
                    'md5': '28f65c8ee6c097986bd902fd4f0804e2',
                },
            ],
            'depends': [
                'dev/build/make',
                'stdenv',
            ],
        },
    }
