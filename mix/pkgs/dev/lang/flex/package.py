def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/westes/flex/releases/download/v2.6.4/flex-2.6.4.tar.lz',
                    'md5': 'a04b480d7455f0f5bdc6d36959e08e4c',
                },
            ],
            'depends': [
                'dev/lang/m4',
                'dev/lang/byacc',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
