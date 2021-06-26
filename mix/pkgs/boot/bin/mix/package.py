def package(mix):
    return {
        'build': {
            'script': mix.files.build_ph,
            'fetch': [
                {
                    'url': 'https://storage.yandexcloud.net/mix-cache/bootstrap-darwin-x86_64.tar.gz',
                    'md5': '163fdaabab2c293d495fe61e617f4909',
                },
            ],
        },
        'runtime': {
            'depends': [
                'env/system',
            ],
        },
    }
