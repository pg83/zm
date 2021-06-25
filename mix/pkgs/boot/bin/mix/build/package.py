def package(mix):
    return {
        'build': {
            'script': mix.files.build_py,
            'depends': [
                'shell/dash',
                'dev/lang/clang',
                'dev/lang/cctools',
            ],
        },
    }
