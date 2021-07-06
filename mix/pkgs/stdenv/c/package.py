def package(mix):
    return {
        'runtime': {
            'depends': [
                'stdenv/c/nort',
                'lib/compiler_rt',
            ],
        },
    }
