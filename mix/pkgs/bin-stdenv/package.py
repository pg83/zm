def package(mix):
    return {
        'runtime': {
            'depends': [
                'boot-make',
                'bin-stdenv-tiny',
            ],
        },
    }