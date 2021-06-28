def package(mix):
    deps = [
        'boot/clang',
    ]

    return {
        'build': {
            'script': mix.files.build_py,
            'depends': deps,
        },
        'runtime': {
            'depends': deps + [
                'boot/sed',
                'boot/gawk',
                'boot/grep',
                'boot/dash',
                'boot/which',
                'boot/coreutils',
                'boot/diffutils',
                'env/bootstrap',
            ],
        },
    }
