def package(mix):
    deps = [
        'boot-which',
        'boot-coreutils',
        'boot-diffutils',
        'boot-dash',
        'boot-gawk',
        'boot-grep',
        'boot-make',
        'boot-sed',
        'boot-clang',
        'boot-cmake',
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
