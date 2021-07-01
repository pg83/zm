def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': [
                'boot/heirloom',
                'boot/bin/stdenv',
            ],
        },
    }
