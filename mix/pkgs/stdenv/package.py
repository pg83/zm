def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': [
                'stdenv/tiny',
            ],
        },
        'runtime': {
            'depends': [
                'tool/compress/xz',
                'tool/compress/gzip',
                'tool/compress/bzip2',
                'tool/compress/unzip',
                'tool/compress/bsdtar',
                'stdenv/tiny',
            ],
        },
    }
