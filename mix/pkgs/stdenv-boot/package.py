def package(mix):
    return {
        'build': {
            'script': mix.files.build_psh,
            'depends': [
                'coreutils-bin',
                'sed-bin',
                'clang-bin',
                'dash-bin',
            ],
        },
    }
