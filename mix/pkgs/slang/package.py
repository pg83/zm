def package(mix):
    libs = [
        'zlib',
        'iconv',
        'readline',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.jedsoft.org/snapshots/slang-pre2.3.3-54.tar.gz',
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
