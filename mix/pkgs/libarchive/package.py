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
                'xz',
                'zlib',
                'bzip2',
                'iconv',
                'gettext',
                'stdenv-tiny',
            ],
        },
    }
