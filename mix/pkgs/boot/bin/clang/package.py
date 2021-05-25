def package(mix):
    return {
        'runtime': {
            'depends': [
                'boot/bin/darwin-clang',
                'env/system',
            ],
        },
    }
