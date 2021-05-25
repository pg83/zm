def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': [
                'lib/bzip2',
                'stdenv/tiny',
            ],
        },
    }
