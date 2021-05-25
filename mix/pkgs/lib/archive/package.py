def package(mix):
    libs = [
        'lib/z',
        'lib/xz',
        'lib/intl',
        'lib/bzip2',
        'lib/iconv',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://libarchive.org/downloads/libarchive-3.5.1.tar.xz',
                },
            ],
            'depends': libs + [
                'stdenv/tiny',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
