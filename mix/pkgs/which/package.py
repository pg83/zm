def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/which/which-2.21.tar.gz',
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
