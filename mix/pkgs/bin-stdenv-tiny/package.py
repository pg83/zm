def package(mix):
    deps = [
        'bin-clang',
        'bin-darwin-coreutils',
        'bin-darwin-sed',
        'bin-darwin-dash',
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
