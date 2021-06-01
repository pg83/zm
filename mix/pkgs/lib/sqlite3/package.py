def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.sqlite.org/2021/sqlite-autoconf-3350500.tar.gz',
                    'md5': 'd1d1aba394c8e0443077dc9f1a681bb8',
                },
            ],
            'depends': [
                'lib/readline',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
