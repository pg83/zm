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
                    'md5': 'e60945d04da8c71a4a888d6c4a8c3fc8',
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
