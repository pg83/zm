def package(mix):
    deps = [
        'which',
        'coreutils',
        'diffutils',
        'dash',
        'gawk',
        'grep',
        'make',
        'sed',
        'clang',
        'cmake',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': deps,
        },
        'runtime': {
            'depends': deps + [
                'env-bootstrap',
            ],
        },
    }
