def package(mix):
    deps = [
        'boot-coreutils',
        'boot-dash',
        'boot-gawk',
        'boot-grep',
        'boot-make',
        'boot-sed',
        'bin-darwin-clang',
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
