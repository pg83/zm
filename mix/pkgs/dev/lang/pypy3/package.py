def package(mix):
    libs = [
        'lib/z',
        'lib/xz',
        'lib/ffi',
        'lib/intl',
        'lib/gdbm',
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
                    'url': 'https://downloads.python.org/pypy/pypy3.7-v7.3.5-src.tar.bz2',
                    'md5': 'dcde1bd64a4c8287b539e6a592166ece',
                },
            ],
            'depends': libs + [
                'dev/build/pkg-config',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
