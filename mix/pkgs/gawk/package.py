def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://mirror.tochlab.net/pub/gnu/gawk/gawk-5.1.0.tar.xz',
                },
            ],
            'depends': [
                'clang',
                'iconv',
                'gettext',
                'boot-stdenv',
            ],
        },
    }
