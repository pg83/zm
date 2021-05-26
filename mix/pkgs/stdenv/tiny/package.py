def package(mix):
    deps = [
        'dev/lang/clang',
        'tool/gnu/which',
        'tool/gnu/coreutils',
        'shell/dash/minimal',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': deps,
        },
        'runtime': {
            'depends': deps + [
                'tool/gnu/sed',
                'tool/gnu/file',
                'tool/gnu/gawk',
                'tool/gnu/grep',
                'tool/gnu/patch',
                'tool/gnu/findutils',
                'tool/gnu/diffutils',
                'dev/build/make',
                'env/bootstrap',
            ],
        },
    }
