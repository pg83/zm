def package(mix):
    return {
        'runtime': {
            'depends': [
                'bzip2',
                'xz',
                'gzip',
                'archive',
                'stdenv-tiny',
            ],
        },
    }
