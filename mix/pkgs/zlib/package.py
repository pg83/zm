def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'http://zlib.net/zlib-1.2.11.tar.xz',
                },
            ],
            'depends': [
                'stdenv-tiny',
            ],
        },
    }
