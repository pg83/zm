def package(mix):
    libs = [
        'lib/z',
        'lib/iconv',
        'lib/readline',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://storage.yandexcloud.net/mix-cache/slang-pre2.3.3-56.tar.gz',
                },
            ],
            'depends': libs + [
                'stdenv',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }