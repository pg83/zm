def package(mix):
    return {
        'runtime': {
            'depends': [
                'bin-darwin-clang',
                'env-system',
            ],
        },
    }
