def package(mix):
    return {
        'build': {
            'script': mix.files.build_ph,
            'fetch': [
                {
                    'url': 'https://storage.yandexcloud.net/mix-cache/bootstrap-darwin-x86_64.tar.gz',
                    'md5': '078767ee51c8e05706adc8f2b5e1e8cf',
                },
            ],
        },
        'runtime': {
            'depends': [
                'env/system',
            ],
        },
    }
