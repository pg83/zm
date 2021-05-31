def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.openssl.org/source/old/1.1.1/openssl-1.1.1j.tar.gz',
                    'md5': 'cccaa064ed860a2b4d1303811bf5c682',
                },
            ],
            'depends': [
                'dev/lang/perl5',
                'stdenv',
            ],
        },
    }
