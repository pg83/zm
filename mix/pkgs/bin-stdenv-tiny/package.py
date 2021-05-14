def package(mix):
    deps = [
        'darwin-env',
        'bin-darwin-coreutils',
        'bin-darwin-sed',
        'bin-darwin-clang',
        'bin-darwin-dash',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': deps,
        },
        'runtime': {
            'depends': deps,
        },
    }
