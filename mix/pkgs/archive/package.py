def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://libarchive.org/downloads/libarchive-3.5.1.tar.xz',
                },
            ],
            'depends': [
                'zlib',
                'bzip2',
                'xz',
                'iconv',
                'gettext',
                'stdenv-tiny',
            ],
        },
    }
