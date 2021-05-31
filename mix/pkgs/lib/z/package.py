def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'http://zlib.net/zlib-1.2.11.tar.xz',
                    'md5': '85adef240c5f370b308da8c938951a68',
                },
            ],
            'depends': [
                'stdenv/tiny',
            ],
        },
    }
