def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://invisible-island.net/datafiles/release/byacc.tar.gz',
                    'md5': 'ad027e9a1a78666e3e27924ce6854f97',
                },
            ],
            'depends': [
                'dev/build/make',
                'stdenv',
            ],
        },
    }
