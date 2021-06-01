def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://mirror.tochlab.net/pub/gnu/help2man/help2man-1.48.3.tar.xz',
                    'md5': 'b51001b5d6c9fc929291d5ae8e6caafc',
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
