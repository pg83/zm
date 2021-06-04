def package(mix):
    deps = [
        'lib/openssl',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://nlnetlabs.nl/downloads/ldns/ldns-1.7.1.tar.gz',
                    'md5': '166262a46995d9972aba417fd091acd5',
                },
            ],
            'depends': deps + [
                'dev/build/make',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': deps,
        },
    }
