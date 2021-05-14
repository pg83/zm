def package(mix):
    deps = [
        'bin-darwin-coreutils',
        'bin-darwin-sed',
        'bin-darwin-clang',
        'bin-darwin-dash',
    ]

    return {
        'build': {
            'script': mix.files.build_ph,
            'depends': deps,
        },
        'runtime': {
            'depends': deps,
        },
    }
