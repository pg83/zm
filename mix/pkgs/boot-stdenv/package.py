def package(mix):
    deps = [
        'darwin-env',
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
            'script': mix.files.build_sh,
            'depends': deps,
        },
        'runtime': {
            'depends': deps,
        },
    }
