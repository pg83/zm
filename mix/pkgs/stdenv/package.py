def package(mix):
    return {
        'build': {
            'script': mix.files.build_py,
        },
        'runtime': {
            'depends': [
                'tool/compress/xz',
                'tool/compress/gzip',
                'tool/compress/bzip2',
                'tool/compress/unzip',
                'tool/compress/bsdtar',
                'stdenv/tiny', # todo: remove env/bootstrap
            ],
        },
    }
