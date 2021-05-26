def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://dist.libuv.org/dist/v1.41.0/libuv-v1.41.0.tar.gz',
                },
            ],
            'depends': [
                'dev/build/autoconf',
                'dev/build/automake',
                'dev/build/libtool',
                'stdenv',
            ],
        },
    }
