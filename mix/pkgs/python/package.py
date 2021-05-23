def package(mix):
    libs = [
        'xz',
        'zlib',
        'bzip2',
        'iconv',
        'expat',
        'libffi',
        'sqlite3',
        'gettext',
        'ncurses',
        'openssl',
        'readline',
        'mpdecimal',
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
                'stdenv',
                'boot-pkg-config',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
