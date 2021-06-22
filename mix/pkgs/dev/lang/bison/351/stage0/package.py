def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/bison/bison-3.5.1.tar.xz',
                    'md5': '6fc5fa4488832a65db934b9e93bd5d4c',
                },
            ],
            'depends': [
                'lib/intl',
                'dev/lang/m4',
                'dev/lang/perl5',
                'dev/lang/bison/341',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
