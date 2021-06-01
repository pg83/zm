def package(mix):
    deps = [
        'dev/lang/clang',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': deps + [
                'boot/stdenv',
            ],
        },
        'runtime': {
            'depends': deps,
        },
    }
