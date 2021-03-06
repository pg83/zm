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
                {
                    'url': 'https://files.pythonhosted.org/packages/0f/86/e19659527668d70be91d0369aeaa055b4eb396b0f387a4f92293a20035bd/pycparser-2.20.tar.gz',
                    'md5': 'b8f88de737db8c346ee8d31c07c7a25a',
                },
            ],
            'depends': libs + [
                'dev/lang/python2',
                'dev/build/pkg-config',
                'dev/build/make',
                'env/compiler',
                'stdenv',
            ],
        },
    }
