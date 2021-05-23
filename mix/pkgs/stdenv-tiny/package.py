def package(mix):
    deps = [
        'clang',
        'which',
        'coreutils',
        'dash-minimal',
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
