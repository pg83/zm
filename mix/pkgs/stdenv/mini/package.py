def package(mix):
    return {
        'runtime': {
            'depends': [
                'stdenv/comp',
                'boot/stdenv',
            ],
        },
    }
