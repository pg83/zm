def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': [
                'lib/curl',
                'stdenv',
            ],
        },
    }
