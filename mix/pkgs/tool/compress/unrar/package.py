def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://storage.yandexcloud.net/mix-cache/unrarsrc-6.0.6.tar.gz',
                    'md5': '4c89e2e5ecfe72a9d96478fb80f38c34',
                },
            ],
            'depends': [
                'lib/cxx',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
