def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://mirror.tochlab.net/pub/gnu/help2man/help2man-1.48.3.tar.xz',
                },
            ],
            'depends': [
                'dev/lang/perl5',
                'dev/build/make',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': [
                'dev/lang/perl5',
            ],
        },
    }
