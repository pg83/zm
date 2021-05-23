def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/pub/gnu/gettext/gettext-0.21.tar.gz',
                },
            ],
            'depends': [
                'boot-stdenv',
                'findutils',
                'gzip',
                'clang',
                'iconv',
            ],
        },
        'runtime': {
            'depends': [
                'iconv',
            ],
        },
    }
