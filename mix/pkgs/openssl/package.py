def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.openssl.org/source/old/1.1.1/openssl-1.1.1j.tar.gz',
                },
            ],
            'depends': [
                'perl5',
                'stdenv',
            ],
        },
    }
