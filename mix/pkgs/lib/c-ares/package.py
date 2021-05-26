def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://c-ares.haxx.se/download/c-ares-1.17.1.tar.gz',
                },
            ],
            'depends': [
                'stdenv',
            ],
        },
    }
