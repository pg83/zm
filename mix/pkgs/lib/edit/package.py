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
                    'url': 'http://thrysoee.dk/editline/libedit-20210522-3.1.tar.gz',
                    'md5': '6ad9e9208daf031adf1ebc64441769e0',
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
