def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/bash/bash-5.1.tar.gz',
                    'md5': 'bb91a17fd6c9032c26d0b2b78b50aff5',
                },
            ],
            'depends': [
                'lib/readline',
                'lib/ncurses',
                'lib/iconv',
                'lib/intl',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
