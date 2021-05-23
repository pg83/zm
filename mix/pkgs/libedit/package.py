def package(mix):
    libs = [
        'ncurses',
        'termcap',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'http://thrysoee.dk/editline/libedit-20210522-3.1.tar.gz',
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
