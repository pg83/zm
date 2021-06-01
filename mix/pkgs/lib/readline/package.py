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
                    'md5': 'e9557dd5b1409f5d7b37ef717c64518e',
                },
            ],
            'depends': libs + [
                'dev/build/make',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
