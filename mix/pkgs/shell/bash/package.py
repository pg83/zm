def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/bash/bash-5.1.tar.gz',
                },
            ],
            'depends': [
                'lib/readline',
                'lib/ncurses',
                'lib/iconv',
                'lib/intl',
                'stdenv',
            ],
        },
    }
