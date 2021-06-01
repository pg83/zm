def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': [
                'boot/bin/darwin/dash',
                'boot/bin/darwin/coreutils',
            ],
        },
    }
