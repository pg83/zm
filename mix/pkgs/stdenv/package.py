def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': [
                'stdenv-tiny',
            ],
        },
        'runtime': {
            'depends': [
                'xz',
                'gzip',
                'bzip2',
                'unzip',
                'gettext',
                'libarchive',
                'stdenv-tiny',
            ],
        },
    }
