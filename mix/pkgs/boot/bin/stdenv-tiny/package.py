def package(mix):
    deps = [
        'boot/bin/clang',
        'boot/bin/darwin-coreutils',
        'boot/bin/darwin-sed',
        'boot/bin/darwin-dash',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': deps,
        },
        'runtime': {
            'depends': deps + [
                'env/bootstrap',
            ],
        },
    }
