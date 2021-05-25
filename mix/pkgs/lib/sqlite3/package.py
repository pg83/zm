def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.sqlite.org/2021/sqlite-autoconf-3350500.tar.gz',
                },
            ],
            'depends': [
                'lib/readline',
                'stdenv',
            ],
        },
    }
