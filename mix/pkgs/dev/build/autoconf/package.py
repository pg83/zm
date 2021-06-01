def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/autoconf/autoconf-2.71.tar.xz',
                },
            ],
            'depends': [
                'dev/lang/m4',
                'dev/lang/perl5',
                'dev/build/make',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': [
                'dev/lang/m4',
            ],
        },
    }
