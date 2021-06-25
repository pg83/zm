def package(mix):
    return {
        'runtime': {
            'depends': [
                'boot/sed',
                'boot/grep',
                'boot/gawk',
                'boot/make',
            ],
        },
    }
