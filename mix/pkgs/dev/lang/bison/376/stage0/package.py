def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/bison/bison-3.7.6.tar.xz',
                    'md5': 'd61aa92e3562cb7292b004ce96173cf7',
                },
            ],
            'depends': [
                'lib/intl',
                'dev/lang/m4',
                'dev/lang/flex',
                'dev/lang/perl5',
                'dev/lang/bison/361/stage1',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
