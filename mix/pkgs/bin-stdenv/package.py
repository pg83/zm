def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': [
                'bin-stdenv-tiny',
            ],
        },
        'runtime': {
            'depends': [
                'boot-make',
                'bin-stdenv-tiny',
            ],
        },
    }
