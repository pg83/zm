def package(mix):
    deps = [
        'boot/which',
        'boot/coreutils',
        'boot/clang',
        'boot/dash',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': deps,
        },
        'runtime': {
            'depends': deps + [
                'boot/diffutils',
                'boot/cctools',
                'boot/gawk',
                'boot/grep',
                'boot/make',
                'boot/sed',
                'env/bootstrap',
            ],
        },
    }
