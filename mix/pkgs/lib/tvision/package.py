def package(mix):
    deps = [
        'lib/cxx',
        'lib/ncurses',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/magiblot/tvision/archive/c36e190174463ece471bdd1c06959fb8dc343c3c.zip',
                    'md5': '9c20bbe1511fe6d8b470f528467e2f27',
                },
            ],
            'depends': deps + [
                'dev/build/cmake',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': deps,
        },
    }
