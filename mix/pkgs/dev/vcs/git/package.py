def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/git/git/archive/refs/tags/v2.32.0-rc1.tar.gz',
                },
            ],
            'depends': [
                'lib/z',
                'lib/curl',
                'lib/iconv',
                'lib/expat',
                'lib/pcre2',
                'lib/openssl',
                'dev/lang/perl5',
                'dev/lang/python3',
                'stdenv',
            ],
        },
    }
