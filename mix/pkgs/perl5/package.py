def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.cpan.org/src/5.0/perl-5.34.0.tar.gz',
                },
            ],
            'depends': [
                'iconv',
                'zlib',
                'coreutils',
                'bash',
                'stdenv',
            ],
        },
    }
