def package(mix):
    libs = [
        'lib/ncurses',
        'lib/termcap',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/readline/readline-8.1.tar.gz',
                },
            ],
            'depends': libs + [
                'stdenv',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
