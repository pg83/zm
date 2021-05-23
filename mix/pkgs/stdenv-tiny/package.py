def package(mix):
    deps = [
        'dash',
        'clang',
        'which',
        'coreutils',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': deps,
        },
        'runtime': {
            'depends': deps + [
                'sed',
                'file',
                'gawk',
                'grep',
                'make',
                'patch',
                'findutils',
                'diffutils',
                'env-bootstrap',
            ],
        },
    }
