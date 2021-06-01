def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.cpan.org/src/5.0/perl-5.34.0.tar.gz',
                    'md5': '2acf2ef147e41730e572251ed079bc1a',
                },
            ],
            'depends': [
                'lib/z',
                'lib/iconv',
                'lib/gdbm',
                'dev/build/make',
                'tool/gnu/coreutils',
                'shell/bash',
                'stdenv',
            ],
        },
    }
