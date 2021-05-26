def package(mix):
    return {
        'runtime': {
            'depends': [
                'boot/make',
                'boot/bin/stdenv/tiny',
            ],
        },
    }
