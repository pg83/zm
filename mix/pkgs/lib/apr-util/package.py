def package(mix):
    deps = [
        'lib/apr',
        'lib/gdbm',
        'lib/iconv',
        'lib/expat',
        'lib/sqlite3',
        'lib/openssl',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://archive.apache.org/dist/apr/apr-util-1.6.1.tar.bz2',
                    'md5': '8ff5dc36fa39a2a3db1df196d3ed6086',
                },
            ],
            'depends': deps + [
                'dev/build/make',
                'dev/build/pkg-config',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': deps,
        },
    }
