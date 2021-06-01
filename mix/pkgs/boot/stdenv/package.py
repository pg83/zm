def package(mix):
    deps = [
        'boot/dash',
        'boot/which',
        'boot/clang',
        'boot/coreutils',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': deps,
        },
        'runtime': {
            'depends': deps + [
                'boot/sed',
                'boot/gawk',
                'boot/grep',
                'boot/diffutils',
                'env/bootstrap',
            ],
        },
    }
