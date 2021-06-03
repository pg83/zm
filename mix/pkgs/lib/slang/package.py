def package(mix):
    libs = [
        'lib/z',
        'lib/pcre',
        'lib/iconv',
        'lib/readline',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://storage.yandexcloud.net/mix-cache/slang-2.3.2.tar.bz2',
                    'md5': 'c2d5a7aa0246627da490be4e399c87cb',
                },
            ],
            'depends': libs + [
                'dev/build/make',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
