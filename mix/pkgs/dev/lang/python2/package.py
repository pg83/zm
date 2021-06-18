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
                    'url': 'https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tar.xz',
                    'md5': 'fd6cc8ec0a78c44036f825e739f36e5a',
                },
            ],
            'depends': libs + [
                'dev/build/make',
                'dev/build/pkg-config',
                'stdenv',
            ],
        },
    }
