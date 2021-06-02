def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/lz4/lz4/archive/refs/tags/v1.9.3.tar.gz',
                    'md5': '3a1ab1684e14fc1afc66228ce61b2db3',
                },
            ],
            'depends': [
                'dev/build/make',
                'stdenv/tiny',
            ],
        },
    }
