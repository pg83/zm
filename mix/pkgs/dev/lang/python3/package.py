def package(mix):
    libs = [
        'lib/z',
        'lib/xz',
        'lib/ffi',
        'lib/intl',
        'lib/bzip2',
        'lib/iconv',
        'lib/expat',
        'lib/sqlite3',
        'lib/ncurses',
        'lib/openssl',
        'lib/readline',
        'lib/mpdecimal',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tar.xz',
                },
            ],
            'depends': libs + [
                'boot/pkg-config',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
