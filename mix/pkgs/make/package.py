def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'http://mirror.keystealth.org/gnu/make/make-4.3.tar.gz',
                },
            ],
            'depends': [
                'clang',
                'boot-stdenv',
            ],
        },
    }
